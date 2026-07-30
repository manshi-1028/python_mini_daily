"""Dashboard page and supporting JSON endpoints (weather, news, currency, AI)."""

from fastapi import APIRouter, Depends, Query, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.core.deps import get_current_user
from app.db.database import get_db
from app.db.models import Expense, User
from app.services.ai import (
    analyze_spending,
    answer_finance_question,
    generate_savings_suggestions,
)
from app.services.analytics import compute_dashboard_summary
from app.services.currency import convert_amount
from app.services.news import get_finance_news
from app.services.weather import get_current_weather

router = APIRouter(tags=["dashboard"])
templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
@router.get("/dashboard", response_class=HTMLResponse)
def dashboard_page(
    request: Request,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Render the main dashboard: totals, charts, recent transactions, widgets."""
    summary = compute_dashboard_summary(db, current_user.id)

    recent_transactions = (
        db.query(Expense)
        .filter(Expense.user_id == current_user.id)
        .order_by(Expense.date.desc())
        .limit(10)
        .all()
    )

    weather = get_current_weather()
    news = get_finance_news(page_size=5)

    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "user": current_user,
            "summary": summary,
            "recent_transactions": recent_transactions,
            "weather": weather,
            "news": news,
        },
    )


@router.get("/api/insights")
def api_insights(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Return Gemini-generated spending analysis and savings suggestions."""
    summary = compute_dashboard_summary(db, current_user.id)
    return {
        "analysis": analyze_spending(
            summary["category_breakdown"], summary["total_expense"]
        ),
        "suggestions": generate_savings_suggestions(
            summary["category_breakdown"],
            summary["total_income"],
            summary["total_expense"],
        ),
    }


@router.post("/api/ask")
def api_ask_finance_question(question: str = Query(..., min_length=3, max_length=500)):
    """Answer a free-form finance question via Gemini."""
    return {"answer": answer_finance_question(question)}


@router.get("/api/convert")
def api_convert_currency(
    amount: float = Query(..., gt=0),
    from_currency: str = Query(..., min_length=3, max_length=3),
    to_currency: str = Query(..., min_length=3, max_length=3),
):
    """Convert an amount between two currencies using live exchange rates."""
    result = convert_amount(amount, from_currency.upper(), to_currency.upper())
    if result is None:
        return {"error": "Conversion unavailable — check EXCHANGE_RATE_API_KEY."}
    return {
        "amount": amount,
        "from": from_currency.upper(),
        "to": to_currency.upper(),
        "result": result,
    }
