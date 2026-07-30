"""
Aggregation logic shared by the dashboard and reports routers.

Kept separate from the routers so both the HTML dashboard and the PDF/CSV
report generation call the exact same numbers — no duplicated arithmetic.
"""

from collections import defaultdict
from datetime import datetime

from sqlalchemy.orm import Session

from app.db.models import Expense, TransactionType


def compute_dashboard_summary(db: Session, user_id: int) -> dict:
    """Compute total income, total expense, balance, and breakdowns for a user."""
    expenses = db.query(Expense).filter(Expense.user_id == user_id).all()

    total_income = sum(
        e.amount for e in expenses if e.transaction_type == TransactionType.INCOME
    )
    total_expense = sum(
        e.amount for e in expenses if e.transaction_type == TransactionType.EXPENSE
    )

    category_breakdown: dict[str, float] = defaultdict(float)
    monthly_trend: dict[str, float] = defaultdict(float)

    for e in expenses:
        if e.transaction_type == TransactionType.EXPENSE:
            category_breakdown[e.category] += e.amount
            month_key = e.date.strftime("%Y-%m")
            monthly_trend[month_key] += e.amount

    return {
        "total_income": round(total_income, 2),
        "total_expense": round(total_expense, 2),
        "balance": round(total_income - total_expense, 2),
        "category_breakdown": dict(sorted(category_breakdown.items())),
        "monthly_trend": dict(sorted(monthly_trend.items())),
    }


def filter_expenses_by_month(
    db: Session, user_id: int, year: int, month: int
) -> list[Expense]:
    """Return all expenses for a user in a given calendar month."""
    expenses = db.query(Expense).filter(Expense.user_id == user_id).all()
    return [e for e in expenses if e.date.year == year and e.date.month == month]


def current_month_key() -> str:
    """Return the current month as 'YYYY-MM', used for default report periods."""
    return datetime.utcnow().strftime("%Y-%m")
