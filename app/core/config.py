"""
Application configuration.

Loads all environment variables through a single Pydantic settings object
so the rest of the codebase never touches os.environ directly.
"""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Strongly typed application settings, populated from environment variables."""

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # --- Core ---
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    ENVIRONMENT: str = "development"
    ALGORITHM: str = "HS256"

    # --- Database ---
    DATABASE_URL: str = "sqlite:///./expense_tracker.db"

    # --- Email ---
    EMAIL_HOST: str = "smtp.gmail.com"
    EMAIL_PORT: int = 587
    EMAIL_ADDRESS: str = ""
    EMAIL_PASSWORD: str = ""

    # --- External APIs ---
    WEATHER_API_KEY: str = ""
    NEWS_API_KEY: str = ""
    EXCHANGE_RATE_API_KEY: str = ""
    GEMINI_API_KEY: str = ""


@lru_cache
def get_settings() -> Settings:
    """Return a cached Settings instance so .env is parsed only once per process."""
    return Settings()


settings = get_settings()
