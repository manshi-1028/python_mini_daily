"""
Google Gemini integration.

Wraps the Gemini API to produce spending-habit analysis, savings
suggestions, and answers to free-form finance questions from the user.
Every function fails soft (returns a fallback string) rather than
raising, since AI features are supplementary to core expense tracking.
"""

import google.generativeai as genai

from app.core.config import settings
from app.core.logging_config import get_logger

logger = get_logger(__name__)

_FALLBACK_MESSAGE = (
    "AI insights are unavailable right now — check that GEMINI_API_KEY is "
    "configured and valid."
)


def _get_model() -> genai.GenerativeModel | None:
    """Configure and return a Gemini model instance, or None if unconfigured."""
    if not settings.GEMINI_API_KEY:
        logger.info("GEMINI_API_KEY not set — AI features disabled")
        return None
    genai.configure(api_key=settings.GEMINI_API_KEY)
    return genai.GenerativeModel("gemini-1.5-flash")


def analyze_spending(category_breakdown: dict[str, float], total_expense: float) -> str:
    """Ask Gemini to analyze a user's spending breakdown and flag concerns."""
    model = _get_model()
    if model is None:
        return _FALLBACK_MESSAGE

    breakdown_text = "\n".join(
        f"- {category}: {amount:.2f}" for category, amount in category_breakdown.items()
    )
    prompt = (
        "You are a personal finance assistant. A user's monthly spending "
        f"breakdown by category is:\n{breakdown_text}\n"
        f"Total expense: {total_expense:.2f}.\n"
        "In under 120 words, identify the top 1-2 categories of concern and "
        "explain briefly why, in plain language."
    )

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as exc:  # Gemini SDK raises various provider-specific errors
        logger.error("Gemini analyze_spending failed: %s", exc)
        return _FALLBACK_MESSAGE


def generate_savings_suggestions(
    category_breakdown: dict[str, float], total_income: float, total_expense: float
) -> str:
    """Ask Gemini for 3 concrete savings suggestions based on the user's numbers."""
    model = _get_model()
    if model is None:
        return _FALLBACK_MESSAGE

    breakdown_text = "\n".join(
        f"- {category}: {amount:.2f}" for category, amount in category_breakdown.items()
    )
    prompt = (
        "You are a personal finance assistant. A user has monthly income "
        f"{total_income:.2f} and monthly expense {total_expense:.2f}, broken "
        f"down as:\n{breakdown_text}\n"
        "Give exactly 3 short, specific, actionable savings suggestions as a "
        "numbered list. No preamble."
    )

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as exc:
        logger.error("Gemini generate_savings_suggestions failed: %s", exc)
        return _FALLBACK_MESSAGE


def answer_finance_question(question: str) -> str:
    """Ask Gemini a free-form personal finance question submitted by the user."""
    model = _get_model()
    if model is None:
        return _FALLBACK_MESSAGE

    prompt = (
        "You are a personal finance assistant embedded in an expense tracker "
        f"app. Answer the following user question in under 150 words, in "
        f"plain, practical language:\n\n{question}"
    )

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as exc:
        logger.error("Gemini answer_finance_question failed: %s", exc)
        return _FALLBACK_MESSAGE
