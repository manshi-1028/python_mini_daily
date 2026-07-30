"""Report generation (PDF/CSV export) and the profile/budgets page."""

import csv
import io
from datetime import datetime

from fastapi import APIRouter, Depends, Query, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.templating import Jinja2Templates
from fpdf import FPDF
from sqlalchemy.orm import Session

from app.core.deps import get_current_user
from app.core.logging_config import get_logger
from app.db.database import get_db
from app.db.models import Budget, User
from app.services.analytics import (
    compute_dashboard_summary,
    current_month_key,
    filter_expenses_by_month,
)
from app.services.charts import render_category_pie_chart, render_monthly_trend_chart
from app.services.email_service import send_monthly_report

router = APIRouter(tags=["reports"])
templates = Jinja2Templates(directory="app/templates")
logger = get_logger(__name__)


@router.get("/reports", response_class=HTMLResponse)
def reports_page(request: Request, current_user: User = Depends(get_current_user)):
    """Render the reports page with export/email controls."""
    return templates.TemplateResponse(
        "reports.html",
        {
            "request": request,
            "user": current_user,
            "current_month": current_month_key(),
        },
    )


@router.get("/reports/csv")
def export_csv(
    year: int = Query(...),
    month: int = Query(..., ge=1, le=12),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Export a month's transactions as a downloadable CSV file."""
    expenses = filter_expenses_by_month(db, current_user.id, year, month)

    buffer = io.StringIO()
    writer = csv.writer(buffer)
    writer.writerow(["Date", "Title", "Category", "Type", "Amount", "Notes"])
    for e in expenses:
        writer.writerow(
            [
                e.date.strftime("%Y-%m-%d"),
                e.title,
                e.category,
                e.transaction_type.value,
                e.amount,
                e.notes or "",
            ]
        )
    buffer.seek(0)

    filename = f"expenses_{year}_{month:02d}.csv"
    logger.info("CSV export generated for user_id=%s: %s", current_user.id, filename)

    return StreamingResponse(
        iter([buffer.getvalue()]),
        media_type="text/csv",
        headers={"Content-Disposition": f"attachment; filename={filename}"},
    )


@router.get("/reports/pdf")
def export_pdf(
    year: int = Query(...),
    month: int = Query(..., ge=1, le=12),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Generate and stream a monthly PDF report with summary charts."""
    pdf_bytes = _build_monthly_pdf(db, current_user, year, month)
    filename = f"expense_report_{year}_{month:02d}.pdf"

    return StreamingResponse(
        iter([pdf_bytes]),
        media_type="application/pdf",
        headers={"Content-Disposition": f"attachment; filename={filename}"},
    )


@router.post("/reports/email")
def email_report(
    year: int = Query(...),
    month: int = Query(..., ge=1, le=12),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Generate the monthly PDF and email it to the logged-in user."""
    pdf_bytes = _build_monthly_pdf(db, current_user, year, month)
    month_label = f"{year}-{month:02d}"
    sent = send_monthly_report(current_user.email, month_label, pdf_bytes)
    return {"sent": sent}


@router.get("/profile", response_class=HTMLResponse)
def profile_page(
    request: Request,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Render the profile page: account info and budget management."""
    budgets = db.query(Budget).filter(Budget.user_id == current_user.id).all()
    return templates.TemplateResponse(
        "profile.html", {"request": request, "user": current_user, "budgets": budgets}
    )


def _build_monthly_pdf(db: Session, user: User, year: int, month: int) -> bytes:
    """Build a monthly PDF report: summary numbers + pie chart + trend chart."""
    summary = compute_dashboard_summary(db, user.id)
    month_expenses = filter_expenses_by_month(db, user.id, year, month)

    pie_png = render_category_pie_chart(summary["category_breakdown"])
    trend_png = render_monthly_trend_chart(summary["monthly_trend"])

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 16)
    pdf.cell(0, 10, f"Expense Report - {year}-{month:02d}", ln=True)

    pdf.set_font("Helvetica", "", 12)
    pdf.cell(0, 8, f"Total Income: {summary['total_income']:.2f}", ln=True)
    pdf.cell(0, 8, f"Total Expense: {summary['total_expense']:.2f}", ln=True)
    pdf.cell(0, 8, f"Balance: {summary['balance']:.2f}", ln=True)
    pdf.ln(4)

    _write_png_to_pdf(pdf, pie_png, w=90)
    _write_png_to_pdf(pdf, trend_png, w=170)

    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(0, 10, "Transactions this month:", ln=True)
    pdf.set_font("Helvetica", "", 10)
    for e in month_expenses:
        line = f"{e.date.strftime('%Y-%m-%d')}  {e.title[:30]:<30}  {e.category:<15}  {e.amount:.2f}"
        pdf.cell(0, 6, line, ln=True)

    return bytes(pdf.output())


def _write_png_to_pdf(pdf: FPDF, png_bytes: bytes, w: float) -> None:
    """Write in-memory PNG bytes into the PDF via a temporary in-memory buffer."""
    image_buffer = io.BytesIO(png_bytes)
    pdf.image(image_buffer, w=w)
    pdf.ln(4)
