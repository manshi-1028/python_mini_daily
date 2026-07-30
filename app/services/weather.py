"""OpenWeather API client."""

import requests

from app.core.config import settings
from app.core.logging_config import get_logger

logger = get_logger(__name__)

WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_current_weather(city: str = "Delhi") -> dict | None:
    """
    Fetch today's weather for a city.

    Returns a small dict with temp/condition/icon, or None on failure —
    callers should treat weather as a "nice to have" widget, not a
    hard dependency.
    """
    if not settings.WEATHER_API_KEY:
        logger.info("WEATHER_API_KEY not set — skipping weather fetch")
        return None

    params = {
        "q": city,
        "appid": settings.WEATHER_API_KEY,
        "units": "metric",
    }

    try:
        response = requests.get(WEATHER_URL, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()
        return {
            "city": data.get("name", city),
            "temperature_c": data["main"]["temp"],
            "condition": data["weather"][0]["description"].title(),
            "icon": data["weather"][0]["icon"],
            "humidity": data["main"]["humidity"],
        }
    except (requests.RequestException, KeyError, IndexError) as exc:
        logger.error("Weather fetch failed for city='%s': %s", city, exc)
        return None
