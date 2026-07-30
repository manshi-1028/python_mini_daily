"""Authentication routes: register, login, logout."""

from fastapi import APIRouter, Depends, Form, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.core.logging_config import get_logger
from app.core.security import (
    COOKIE_NAME,
    create_access_token,
    hash_password,
    verify_password,
)
from app.db.database import get_db
from app.db.models import User

router = APIRouter(tags=["auth"])
templates = Jinja2Templates(directory="app/templates")
logger = get_logger(__name__)


@router.get("/register", response_class=HTMLResponse)
def register_page(request: Request) -> HTMLResponse:
    """Render the registration form."""
    return templates.TemplateResponse(
        "register.html", {"request": request, "error": None}
    )


@router.post("/register")
def register_submit(
    request: Request,
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db),
):
    """Handle registration form submission."""
    existing = (
        db.query(User)
        .filter((User.username == username) | (User.email == email))
        .first()
    )

    if existing:
        logger.info(
            "Registration rejected: username/email already taken (%s)", username
        )
        return templates.TemplateResponse(
            "register.html",
            {"request": request, "error": "Username or email already registered."},
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    user = User(
        username=username,
        email=email,
        hashed_password=hash_password(password),
    )
    db.add(user)
    db.commit()
    logger.info("New user registered: %s", username)

    return RedirectResponse(url="/login", status_code=status.HTTP_303_SEE_OTHER)


@router.get("/login", response_class=HTMLResponse)
def login_page(request: Request) -> HTMLResponse:
    """Render the login form."""
    return templates.TemplateResponse("login.html", {"request": request, "error": None})


@router.post("/login")
def login_submit(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db),
):
    """Verify credentials and set the JWT auth cookie."""
    user = db.query(User).filter(User.username == username).first()

    if not user or not verify_password(password, user.hashed_password):
        logger.warning("Failed login attempt for username='%s'", username)
        return templates.TemplateResponse(
            "login.html",
            {"request": request, "error": "Invalid username or password."},
            status_code=status.HTTP_401_UNAUTHORIZED,
        )

    token = create_access_token(data={"sub": user.username})
    response = RedirectResponse(url="/dashboard", status_code=status.HTTP_303_SEE_OTHER)
    response.set_cookie(
        key=COOKIE_NAME,
        value=token,
        httponly=True,
        samesite="lax",
        max_age=60 * 60,
    )
    logger.info("User logged in: %s", username)
    return response


@router.get("/logout")
def logout():
    """Clear the auth cookie and redirect to login."""
    response = RedirectResponse(url="/login", status_code=status.HTTP_303_SEE_OTHER)
    response.delete_cookie(COOKIE_NAME)
    return response
