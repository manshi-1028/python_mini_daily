"""Expense CRUD routes, plus budget creation and alerting."""

from fastapi import APIRouter, Depends, Form, HTTPException, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.core.deps import get_current_user
from app.core.logging_config import get_logger
from app.db.database import get_db
from app.db.models import Budget, Expense, RecurrenceInterval, TransactionType, User
from app.services.analytics import compute_dashboard_summary
from app.services.email_service import send_budget_alert

router = APIRouter(tags=["expenses"])
templates = Jinja2Templates(directory="app/templates")
logger = get_logger(__name__)


@router.get("/expenses/add", response_class=HTMLResponse)
def add_expense_page(request: Request, current_user: User = Depends(get_current_user)):
    """Render the add-expense form."""
    return templates.TemplateResponse(
        "add_expense.html", {"request": request, "user": current_user, "error": None}
    )


@router.post("/expenses/add")
def add_expense_submit(
    title: str = Form(...),
    amount: float = Form(...),
    category: str = Form(...),
    transaction_type: TransactionType = Form(TransactionType.EXPENSE),
    notes: str = Form(""),
    is_recurring: bool = Form(False),
    recurrence_interval: RecurrenceInterval = Form(RecurrenceInterval.NONE),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Persist a new expense/income entry, then check budget limits."""
    expense = Expense(
        user_id=current_user.id,
        title=title,
        amount=amount,
        category=category,
        transaction_type=transaction_type,
        notes=notes or None,
        is_recurring=is_recurring,
        recurrence_interval=recurrence_interval,
    )
    db.add(expense)
    db.commit()
    logger.info(
        "Expense added for user_id=%s: %s (%.2f)", current_user.id, title, amount
    )

    _check_budget_and_alert(db, current_user, category)

    return RedirectResponse(url="/dashboard", status_code=status.HTTP_303_SEE_OTHER)


@router.get("/expenses/{expense_id}/edit", response_class=HTMLResponse)
def edit_expense_page(
    expense_id: int,
    request: Request,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Render the edit form for a single expense, scoped to its owner."""
    expense = _get_owned_expense_or_404(db, expense_id, current_user.id)
    return templates.TemplateResponse(
        "edit_expense.html",
        {"request": request, "user": current_user, "expense": expense, "error": None},
    )


@router.post("/expenses/{expense_id}/edit")
def edit_expense_submit(
    expense_id: int,
    title: str = Form(...),
    amount: float = Form(...),
    category: str = Form(...),
    transaction_type: TransactionType = Form(...),
    notes: str = Form(""),
    is_recurring: bool = Form(False),
    recurrence_interval: RecurrenceInterval = Form(RecurrenceInterval.NONE),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Apply edits to an existing expense, scoped to its owner."""
    expense = _get_owned_expense_or_404(db, expense_id, current_user.id)

    expense.title = title
    expense.amount = amount
    expense.category = category
    expense.transaction_type = transaction_type
    expense.notes = notes or None
    expense.is_recurring = is_recurring
    expense.recurrence_interval = recurrence_interval

    db.commit()
    logger.info("Expense id=%s updated by user_id=%s", expense_id, current_user.id)

    _check_budget_and_alert(db, current_user, category)

    return RedirectResponse(url="/dashboard", status_code=status.HTTP_303_SEE_OTHER)


@router.post("/expenses/{expense_id}/delete")
def delete_expense(
    expense_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Delete an expense, scoped to its owner."""
    expense = _get_owned_expense_or_404(db, expense_id, current_user.id)
    db.delete(expense)
    db.commit()
    logger.info("Expense id=%s deleted by user_id=%s", expense_id, current_user.id)
    return RedirectResponse(url="/dashboard", status_code=status.HTTP_303_SEE_OTHER)


@router.post("/budgets/add")
def add_budget(
    category: str = Form(...),
    monthly_limit: float = Form(...),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Create or update a monthly budget limit for a category."""
    existing = (
        db.query(Budget)
        .filter(Budget.user_id == current_user.id, Budget.category == category)
        .first()
    )
    if existing:
        existing.monthly_limit = monthly_limit
    else:
        db.add(
            Budget(
                user_id=current_user.id, category=category, monthly_limit=monthly_limit
            )
        )
    db.commit()
    logger.info(
        "Budget set for user_id=%s category=%s limit=%.2f",
        current_user.id,
        category,
        monthly_limit,
    )
    return RedirectResponse(url="/profile", status_code=status.HTTP_303_SEE_OTHER)


def _get_owned_expense_or_404(db: Session, expense_id: int, user_id: int) -> Expense:
    """Fetch an expense and verify it belongs to the given user, or raise 404."""
    expense = db.query(Expense).filter(Expense.id == expense_id).first()
    if expense is None or expense.user_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Expense not found"
        )
    return expense


def _check_budget_and_alert(db: Session, user: User, category: str) -> None:
    """If spend in `category` exceeds its budget this month, email an alert."""
    budget = (
        db.query(Budget)
        .filter(Budget.user_id == user.id, Budget.category == category)
        .first()
    )
    if budget is None:
        return

    summary = compute_dashboard_summary(db, user.id)
    spent = summary["category_breakdown"].get(category, 0.0)

    if spent > budget.monthly_limit:
        send_budget_alert(user.email, category, budget.monthly_limit, spent)
        logger.info(
            "Budget exceeded for user_id=%s category=%s spent=%.2f limit=%.2f",
            user.id,
            category,
            spent,
            budget.monthly_limit,
        )
