"""
Shared FastAPI dependencies, primarily authentication.

`get_current_user` reads the JWT from the httponly cookie set at login,
decodes it, and loads the corresponding user row. Route handlers depend
on this instead of touching cookies/tokens directly.
"""

from fastapi import Cookie, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.logging_config import get_logger
from app.core.security import COOKIE_NAME, decode_access_token
from app.db.database import get_db
from app.db.models import User

logger = get_logger(__name__)


def get_current_user(
    access_token: str | None = Cookie(default=None, alias=COOKIE_NAME),
    db: Session = Depends(get_db),
) -> User:
    """Resolve the currently logged-in user from the auth cookie, or raise 401."""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Not authenticated",
        headers={"Location": "/login"},
    )

    if access_token is None:
        raise credentials_exception

    payload = decode_access_token(access_token)
    if payload is None:
        raise credentials_exception

    username: str | None = payload.get("sub")
    if username is None:
        raise credentials_exception

    user = db.query(User).filter(User.username == username).first()
    if user is None or not user.is_active:
        logger.warning("Auth cookie valid but user '%s' not found/inactive", username)
        raise credentials_exception

    return user


def get_current_user_optional(
    access_token: str | None = Cookie(default=None, alias=COOKIE_NAME),
    db: Session = Depends(get_db),
) -> User | None:
    """Like get_current_user but returns None instead of raising (for public pages)."""
    if access_token is None:
        return None
    payload = decode_access_token(access_token)
    if payload is None:
        return None
    username = payload.get("sub")
    if username is None:
        return None
    return db.query(User).filter(User.username == username).first()
