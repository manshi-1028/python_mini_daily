"""Pydantic schemas for expense and budget CRUD."""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from app.db.models import RecurrenceInterval, TransactionType


class ExpenseCreate(BaseModel):
    """Payload for creating a new expense/income entry."""

    title: str = Field(min_length=1, max_length=150)
    amount: float = Field(gt=0)
    category: str = Field(min_length=1, max_length=50)
    transaction_type: TransactionType = TransactionType.EXPENSE
    notes: str | None = Field(default=None, max_length=500)
    is_recurring: bool = False
    recurrence_interval: RecurrenceInterval = RecurrenceInterval.NONE
    date: datetime | None = None


class ExpenseUpdate(BaseModel):
    """Payload for editing an existing expense. All fields optional."""

    title: str | None = Field(default=None, min_length=1, max_length=150)
    amount: float | None = Field(default=None, gt=0)
    category: str | None = Field(default=None, min_length=1, max_length=50)
    transaction_type: TransactionType | None = None
    notes: str | None = Field(default=None, max_length=500)
    is_recurring: bool | None = None
    recurrence_interval: RecurrenceInterval | None = None
    date: datetime | None = None


class ExpenseRead(BaseModel):
    """Public representation of an expense."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    amount: float
    category: str
    transaction_type: TransactionType
    notes: str | None
    is_recurring: bool
    recurrence_interval: RecurrenceInterval
    date: datetime
    created_at: datetime


class BudgetCreate(BaseModel):
    """Payload for setting a monthly budget limit for a category."""

    category: str = Field(min_length=1, max_length=50)
    monthly_limit: float = Field(gt=0)


class BudgetRead(BaseModel):
    """Public representation of a budget."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    category: str
    monthly_limit: float
    created_at: datetime


class DashboardSummary(BaseModel):
    """Aggregated numbers shown on the dashboard."""

    total_income: float
    total_expense: float
    balance: float
    category_breakdown: dict[str, float]
    monthly_trend: dict[str, float]
