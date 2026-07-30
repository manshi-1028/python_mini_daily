"""
Matplotlib chart generation.

Charts are rendered server-side to PNG bytes (used inside PDF reports).
The live dashboard instead uses Chart.js in the browser — see
static/js/dashboard.js — since client-side charts don't need a round trip.
"""

import io

import matplotlib

matplotlib.use("Agg")  # headless backend — no display server in a container
import matplotlib.pyplot as plt  # noqa: E402


def render_category_pie_chart(category_breakdown: dict[str, float]) -> bytes:
    """Render a pie chart of spend-by-category and return PNG bytes."""
    fig, ax = plt.subplots(figsize=(5, 5))

    if category_breakdown:
        ax.pie(
            list(category_breakdown.values()),
            labels=list(category_breakdown.keys()),
            autopct="%1.1f%%",
            startangle=90,
        )
    else:
        ax.text(0.5, 0.5, "No data", ha="center", va="center")
    ax.set_title("Spending by Category")

    return _figure_to_png_bytes(fig)


def render_monthly_trend_chart(monthly_trend: dict[str, float]) -> bytes:
    """Render a bar chart of monthly totals and return PNG bytes."""
    fig, ax = plt.subplots(figsize=(7, 4))

    if monthly_trend:
        months = list(monthly_trend.keys())
        values = list(monthly_trend.values())
        ax.bar(months, values, color="#4C72B0")
        ax.set_ylabel("Amount")
        plt.xticks(rotation=45, ha="right")
    else:
        ax.text(0.5, 0.5, "No data", ha="center", va="center")
    ax.set_title("Monthly Trend")
    fig.tight_layout()

    return _figure_to_png_bytes(fig)


def _figure_to_png_bytes(fig: plt.Figure) -> bytes:
    """Serialize a Matplotlib figure to PNG bytes and close it to free memory."""
    buffer = io.BytesIO()
    fig.savefig(buffer, format="png", dpi=150)
    plt.close(fig)
    buffer.seek(0)
    return buffer.read()
