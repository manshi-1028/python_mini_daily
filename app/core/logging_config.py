"""
Logging configuration.

Sets up a rotating file handler writing to logs/app.log plus a console
handler, so both local development and container logs are useful.
"""

import logging
import os
from logging.handlers import RotatingFileHandler

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "app.log")


def configure_logging() -> None:
    """Configure root logging handlers. Safe to call multiple times (idempotent)."""
    os.makedirs(LOG_DIR, exist_ok=True)

    root_logger = logging.getLogger()
    if root_logger.handlers:
        # Already configured (e.g. reloader re-import) — don't duplicate handlers.
        return

    root_logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    file_handler = RotatingFileHandler(
        LOG_FILE, maxBytes=5 * 1024 * 1024, backupCount=3
    )
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)


def get_logger(name: str) -> logging.Logger:
    """Return a module-level logger. Call configure_logging() once at startup first."""
    return logging.getLogger(name)
