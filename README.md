# AI Expense Tracker

A full-stack personal expense tracker built with **FastAPI**, **SQLAlchemy**, and **Jinja2**, with AI-powered spending insights via **Google Gemini**, live weather/news/currency widgets, and monthly PDF/CSV reporting.

## Features

- **Auth**: register, login, logout — JWT stored in an httponly cookie, bcrypt password hashing
- **Expense management**: add / edit / delete transactions, categories, income vs. expense, recurring transactions, monthly budgets with email alerts
- **Dashboard**: total income/expense/balance, category pie chart, monthly trend bar chart (Chart.js), recent transactions
- **Reports**: monthly PDF (with embedded Matplotlib charts) and CSV export, plus emailing the PDF report via SMTP
- **AI insights**: Gemini-powered spending analysis, savings suggestions, and free-form finance Q&A
- **External APIs**: OpenWeather (today's weather), NewsAPI (finance headlines), ExchangeRate API (currency conversion)
- **Testing**: Pytest suite covering auth and expense CRUD, run against an isolated in-memory SQLite DB
- **Deployment**: Dockerfile + docker-compose, GitHub Actions CI (lint + test on every push)

## Tech Stack

Python 3.13 · FastAPI · SQLAlchemy · SQLite · Jinja2 · Bootstrap 5 · Chart.js · Matplotlib · fpdf2 · Google Gemini API · OpenWeather API · ExchangeRate API · NewsAPI · Pytest · Docker

## Folder Structure

```
AI-Expense-Tracker/
├── app/
│   ├── main.py                # FastAPI app entrypoint
│   ├── core/                  # config, security, logging, shared deps
│   ├── db/                    # SQLAlchemy engine + models
│   ├── schemas/                # Pydantic request/response schemas
│   ├── routers/                # auth, expenses, dashboard, reports
│   ├── services/                # ai, email, charts, currency, news, weather, analytics
│   ├── templates/              # Jinja2 HTML templates
│   └── static/                 # CSS/JS assets
├── tests/                     # Pytest suite
├── .github/workflows/ci.yml   # CI pipeline
├── requirements.txt
├── .env.example
├── Dockerfile
├── docker-compose.yml
└── LICENSE
```

## Installation (local)

```bash
git clone https://github.com/<your-username>/AI-Expense-Tracker.git
cd AI-Expense-Tracker

python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

pip install -r requirements.txt

cp .env.example .env            # then fill in SECRET_KEY and any API keys you have

uvicorn app.main:app --reload
```

Visit `http://localhost:8000/register` to create an account.

## API Keys

All external integrations degrade gracefully if a key is missing — the app runs fine with just `SECRET_KEY` set; weather/news/currency/AI widgets simply show as unavailable.

| Variable | Where to get it |
|---|---|
| `WEATHER_API_KEY` | [openweathermap.org/api](https://openweathermap.org/api) |
| `NEWS_API_KEY` | [newsapi.org](https://newsapi.org) |
| `EXCHANGE_RATE_API_KEY` | [exchangerate-api.com](https://www.exchangerate-api.com) |
| `GEMINI_API_KEY` | [ai.google.dev](https://ai.google.dev) |
| `EMAIL_ADDRESS` / `EMAIL_PASSWORD` | Gmail App Password (not your regular password) |

## Running Tests

```bash
pytest -v
```

## Deployment (Docker)

```bash
docker compose up --build
```

The app will be available at `http://localhost:8000`.

## Screenshots

_Add screenshots to `/screenshots` and reference them here once you have a running instance._

## Future Improvements

- Recurring transaction auto-generation via a scheduled job (APScheduler/Celery)
- Multi-currency account support (store transactions in native currency + display currency)
- OAuth login (Google/GitHub)
- Role-based multi-user households / shared budgets

## License

MIT — see [LICENSE](LICENSE).
