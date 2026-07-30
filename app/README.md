# Expense Tracker API

This directory contains the main FastAPI application for the Expense Tracker project. It includes the API, business logic, database configuration, templates, static assets, and automated tests.

---

## Directory Structure

```
app/
├── .github/
│   └── workflows/
│       └── ci.yml
├── core/
├── db/
├── routers/
├── schemas/
├── services/
├── static/
│   └── css/
├── templates/
├── tests/
├── .dockerignore
├── .env.example
├── Dockerfile
├── requirements.txt
└── main.py
```

---

## Features

- Expense CRUD operations
- FastAPI REST API
- HTML templates (Jinja2)
- Static CSS support
- Database integration
- Pydantic request/response validation
- Service layer architecture
- Automated tests with Pytest
- GitHub Actions CI
- Docker support

---

## Project Architecture

### `core/`
Application configuration, settings, and shared utilities.

### `db/`
Database connection, models, and session management.

### `routers/`
API route definitions and endpoint logic.

### `schemas/`
Pydantic models used for request validation and API responses.

### `services/`
Business logic separated from route handlers.

### `templates/`
Jinja2 HTML templates rendered by FastAPI.

### `static/`
Static assets such as CSS files.

### `tests/`
Unit and integration tests for API endpoints and application logic.

---

## Running the Application

Install dependencies

```bash
pip install -r requirements.txt
```

Run the development server

```bash
uvicorn main:app --reload
```

The application will be available at

```
http://127.0.0.1:8000
```

Interactive API documentation

```
http://127.0.0.1:8000/docs
```

---

## Running Tests

Execute all tests

```bash
pytest
```

Run with verbose output

```bash
pytest -v
```

---

## Continuous Integration

GitHub Actions automatically:

- Installs dependencies
- Runs the test suite
- Verifies successful builds on every push and pull request

Workflow file:

```
.github/workflows/ci.yml
```

---

## Docker

Build the image

```bash
docker build -t expense-tracker .
```

Run the container

```bash
docker run -p 8000:8000 expense-tracker
```

---

## Environment Variables

Create a `.env` file using the provided example.

```
cp .env.example .env
```

Update the required environment variables before running the application.

---

## Tech Stack

- FastAPI
- Python
- Pydantic
- Jinja2
- Pytest
- Docker
- GitHub Actions

---

## License

This project is intended for learning and educational purposes.
