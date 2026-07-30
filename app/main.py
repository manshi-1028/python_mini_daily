"""
Application entrypoint.

Creates the FastAPI app, wires up static files, templates, routers,
DB initialization, and logging. Run with:

    uvicorn app.main:app --reload
"""

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.core.logging_config import configure_logging, get_logger
from app.db.database import init_db
from app.routers import auth, dashboard, expenses, reports

configure_logging()
logger = get_logger(__name__)

app = FastAPI(
    title="AI Expense Tracker",
    description="A FastAPI-based personal expense tracker with AI-powered insights.",
    version="1.0.0",
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(auth.router)
app.include_router(dashboard.router)
app.include_router(expenses.router)
app.include_router(reports.router)


@app.on_event("startup")
def on_startup() -> None:
    """Initialize the database schema on application startup."""
    init_db()
    logger.info("Application startup complete — database initialized.")


@app.get("/health", tags=["meta"])
def health_check() -> dict[str, str]:
    """Simple liveness endpoint for uptime checks / container healthchecks."""
    return {"status": "ok"}
