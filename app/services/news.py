"""NewsAPI client for finance headlines."""

import requests

from app.core.config import settings
from app.core.logging_config import get_logger

logger = get_logger(__name__)

NEWS_URL = "https://newsapi.org/v2/top-headlines"


def get_finance_news(page_size: int = 5) -> list[dict]:
    """Fetch the latest finance headlines. Returns an empty list on failure."""
    if not settings.NEWS_API_KEY:
        logger.info("NEWS_API_KEY not set — skipping news fetch")
        return []

    params = {
        "category": "business",
        "language": "en",
        "pageSize": page_size,
        "apiKey": settings.NEWS_API_KEY,
    }

    try:
        response = requests.get(NEWS_URL, params=params, timeout=5)
        response.raise_for_status()
        articles = response.json().get("articles", [])
        return [
            {
                "title": a.get("title"),
                "source": a.get("source", {}).get("name"),
                "url": a.get("url"),
                "published_at": a.get("publishedAt"),
            }
            for a in articles
        ]
    except requests.RequestException as exc:
        logger.error("News fetch failed: %s", exc)
        return []
