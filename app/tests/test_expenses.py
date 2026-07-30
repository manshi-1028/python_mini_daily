"""Tests for expense CRUD and dashboard aggregation."""

import pytest


@pytest.fixture
def auth_cookie(client):
    """Register + login a user, return their auth cookie dict."""
    client.post(
        "/register",
        data={"username": "bob", "email": "bob@example.com", "password": "strongpass123"},
    )
    login_response = client.post(
        "/login", data={"username": "bob", "password": "strongpass123"}, follow_redirects=False
    )
    return {"access_token": login_response.cookies["access_token"]}


def test_add_expense_creates_transaction(client, auth_cookie):
    response = client.post(
        "/expenses/add",
        data={
            "title": "Groceries",
            "amount": "150.50",
            "category": "Food",
            "transaction_type": "expense",
        },
        cookies=auth_cookie,
        follow_redirects=False,
    )
    assert response.status_code == 303

    dashboard = client.get("/dashboard", cookies=auth_cookie)
    assert "Groceries" in dashboard.text
    assert "150.50" in dashboard.text


def test_add_income_reflected_in_balance(client, auth_cookie):
    client.post(
        "/expenses/add",
        data={"title": "Salary", "amount": "50000", "category": "Salary", "transaction_type": "income"},
        cookies=auth_cookie,
    )
    client.post(
        "/expenses/add",
        data={"title": "Rent", "amount": "15000", "category": "Rent", "transaction_type": "expense"},
        cookies=auth_cookie,
    )

    dashboard = client.get("/dashboard", cookies=auth_cookie)
    assert "35000.00" in dashboard.text  # balance = 50000 - 15000


def test_edit_expense_updates_fields(client, auth_cookie):
    client.post(
        "/expenses/add",
        data={"title": "Coffee", "amount": "5", "category": "Food", "transaction_type": "expense"},
        cookies=auth_cookie,
    )

    edit_response = client.post(
        "/expenses/1/edit",
        data={"title": "Coffee (updated)", "amount": "6", "category": "Food", "transaction_type": "expense"},
        cookies=auth_cookie,
        follow_redirects=False,
    )
    assert edit_response.status_code == 303

    dashboard = client.get("/dashboard", cookies=auth_cookie)
    assert "Coffee (updated)" in dashboard.text


def test_delete_expense_removes_it(client, auth_cookie):
    client.post(
        "/expenses/add",
        data={"title": "Snacks", "amount": "20", "category": "Food", "transaction_type": "expense"},
        cookies=auth_cookie,
    )

    delete_response = client.post("/expenses/1/delete", cookies=auth_cookie, follow_redirects=False)
    assert delete_response.status_code == 303

    dashboard = client.get("/dashboard", cookies=auth_cookie)
    assert "Snacks" not in dashboard.text


def test_editing_expense_owned_by_another_user_returns_404(client, auth_cookie):
    client.post(
        "/expenses/add",
        data={"title": "Bob's item", "amount": "10", "category": "Misc", "transaction_type": "expense"},
        cookies=auth_cookie,
    )

    client.post(
        "/register",
        data={"username": "carol", "email": "carol@example.com", "password": "strongpass123"},
    )
    carol_login = client.post(
        "/login", data={"username": "carol", "password": "strongpass123"}, follow_redirects=False
    )
    carol_cookie = {"access_token": carol_login.cookies["access_token"]}

    response = client.get("/expenses/1/edit", cookies=carol_cookie)
    assert response.status_code == 404
