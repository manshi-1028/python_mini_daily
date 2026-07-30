"""Tests for registration, login, logout, and route protection."""


def _register(client, username="alice", email="alice@example.com", password="strongpass123"):
    return client.post(
        "/register",
        data={"username": username, "email": email, "password": password},
        follow_redirects=False,
    )


def _login(client, username="alice", password="strongpass123"):
    return client.post(
        "/login",
        data={"username": username, "password": password},
        follow_redirects=False,
    )


def test_register_success_redirects_to_login(client):
    response = _register(client)
    assert response.status_code == 303
    assert response.headers["location"] == "/login"


def test_register_duplicate_username_rejected(client):
    _register(client)
    response = _register(client, email="different@example.com")
    assert response.status_code == 400
    assert "already registered" in response.text


def test_login_success_sets_cookie_and_redirects(client):
    _register(client)
    response = _login(client)
    assert response.status_code == 303
    assert response.headers["location"] == "/dashboard"
    assert "access_token" in response.cookies


def test_login_wrong_password_rejected(client):
    _register(client)
    response = _login(client, password="wrongpassword")
    assert response.status_code == 401
    assert "Invalid username or password" in response.text


def test_dashboard_requires_auth(client):
    response = client.get("/dashboard", follow_redirects=False)
    assert response.status_code == 401


def test_dashboard_accessible_after_login(client):
    _register(client)
    login_response = _login(client)
    token = login_response.cookies["access_token"]

    response = client.get("/dashboard", cookies={"access_token": token})
    assert response.status_code == 200
    assert "Welcome, alice" in response.text


def test_logout_clears_cookie(client):
    _register(client)
    login_response = _login(client)
    token = login_response.cookies["access_token"]

    response = client.get("/logout", cookies={"access_token": token}, follow_redirects=False)
    assert response.status_code == 303
    assert response.headers["location"] == "/login"
