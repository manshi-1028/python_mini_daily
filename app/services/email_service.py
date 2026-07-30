"""
SMTP email service.

Handles monthly report emails and budget-alert notifications.
Uses stdlib smtplib/email so no extra dependency is needed.
"""

import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from app.core.config import settings
from app.core.logging_config import get_logger

logger = get_logger(__name__)


def _send_email(
    to_address: str,
    subject: str,
    body: str,
    attachment_bytes: bytes | None = None,
    attachment_filename: str | None = None,
) -> bool:
    """Send an email via SMTP. Returns True on success, False on any failure."""
    if not settings.EMAIL_ADDRESS or not settings.EMAIL_PASSWORD:
        logger.info("EMAIL_ADDRESS/EMAIL_PASSWORD not set — skipping email send")
        return False

    message = MIMEMultipart()
    message["From"] = settings.EMAIL_ADDRESS
    message["To"] = to_address
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    if attachment_bytes and attachment_filename:
        part = MIMEApplication(attachment_bytes, Name=attachment_filename)
        part["Content-Disposition"] = f'attachment; filename="{attachment_filename}"'
        message.attach(part)

    try:
        with smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT) as server:
            server.starttls()
            server.login(settings.EMAIL_ADDRESS, settings.EMAIL_PASSWORD)
            server.sendmail(settings.EMAIL_ADDRESS, to_address, message.as_string())
        logger.info("Email sent to %s: %s", to_address, subject)
        return True
    except smtplib.SMTPException as exc:
        logger.error("Failed to send email to %s: %s", to_address, exc)
        return False


def send_monthly_report(to_address: str, month_label: str, pdf_bytes: bytes) -> bool:
    """Email a generated monthly PDF report to the user."""
    return _send_email(
        to_address=to_address,
        subject=f"Your Expense Report — {month_label}",
        body=(
            f"Hi,\n\nAttached is your expense report for {month_label}.\n\n"
            "— AI Expense Tracker"
        ),
        attachment_bytes=pdf_bytes,
        attachment_filename=f"expense_report_{month_label}.pdf",
    )


def send_budget_alert(
    to_address: str, category: str, limit: float, spent: float
) -> bool:
    """Email the user when spending in a category exceeds its budget limit."""
    return _send_email(
        to_address=to_address,
        subject=f"Budget Alert: {category} limit exceeded",
        body=(
            f"Hi,\n\nYou've spent {spent:.2f} in '{category}', which exceeds "
            f"your monthly limit of {limit:.2f}.\n\n"
            "— AI Expense Tracker"
        ),
    )
