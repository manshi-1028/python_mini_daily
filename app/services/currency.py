"""ExchangeRate API client for currency conversion."""

import requests

from app.core.config import settings
from app.core.logging_config import get_logger

logger = get_logger(__name__)

BASE_URL = "https://v6.exchangerate-api.com/v6"


def get_exchange_rates(base_currency: str = "INR") -> dict[str, float] | None:
    """Fetch latest exchange rates for a base currency. Returns None on failure."""
    if not settings.EXCHANGE_RATE_API_KEY:
        logger.info("EXCHANGE_RATE_API_KEY not set — skipping rate fetch")
        return None

    url = f"{BASE_URL}/{settings.EXCHANGE_RATE_API_KEY}/latest/{base_currency}"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        if data.get("result") != "success":
            logger.error("Exchange rate API returned error payload: %s", data)
            return None
        return data.get("conversion_rates")
    except requests.RequestException as exc:
        logger.error("Exchange rate fetch failed: %s", exc)
        return None


def convert_amount(amount: float, from_currency: str, to_currency: str) -> float | None:
    """Convert an amount between two currencies using live rates. None on failure."""
    rates = get_exchange_rates(base_currency=from_currency)
    if rates is None or to_currency not in rates:
        return None
    return round(amount * rates[to_currency], 2)
