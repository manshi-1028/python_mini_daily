# Python Mini Daily

Daily practice projects from **100 Days of Code: The Complete Python Pro Bootcamp** (Angela Yu) — one mini-project per day, from Python fundamentals all the way to Flask web apps — plus a larger FastAPI project built alongside the course.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

## Repository layout

- **`Day4/` … `Day61/`** — course mini-projects, one folder per day (see tables below)
- **`app/`** — Expense Tracker, a full FastAPI web app (auth, CRUD, analytics, Docker)
- **`Dockerfile` / `docker-compose.yml` / `requirements.txt`** (repo root) — copies of the app's build files for one-command setup
- **`tests/`** — pytest suite for the app (mirrors `app/tests/`)

> Folder naming follows whatever the course download used on a given day — some are day-numbered (`Day55/`), some are project names only. A few folder names have typos from the original course zips (`monady motivation`, `passward manager`, `daily umbrella remider `) — they're kept as-is so paths don't break.

---

## Course projects

### Days 1–30 — Python fundamentals → intermediate

| Folder | Project | Concepts practiced |
| --- | --- | --- |
| `Day4` | Day 4 exercises | randomisation, lists, loops |
| `Day 10/Calculator Project` | Calculator | functions, return values, recursion |
| `day 11 black jack game` | Blackjack (capstone) | game logic, while loops |
| `day 12 number guessing` | Number Guessing | global/local scope |
| `day 14` | Higher / Lower | dictionaries, game loop |
| `Day 15` | Coffee Machine (procedural) | while loops, resources, money handling |
| `Day - 16/oop-coffee-machine-start` | Coffee Machine (OOP) | classes, attributes, methods |
| `quiz-game-start` | Quiz | OOP: Question model + QuizBrain |
| `Hirst Painting Project` | Hirst-Style Dot Painting | Turtle graphics, colour extraction |
| `turtle race` | Turtle Race | event listeners, Turtle graphics |
| `PythonProject1` | Snake | OOP game loop, scoreboard, high-score file |
| `pingpong` | Pong | collision detection, ball physics |
| `turtle crossing` | Turtle Crossing | timers, difficulty scaling |
| `Mail+Merge+Project+Start` | Mail Merge | file I/O, string templating |
| `us game` | US States Game | pandas + Turtle, CSV read/write |
| `NATO-Alphabet-Project` | NATO Phonetic Alphabet | dict comprehension, error handling |
| `passward manager` | Password Manager | Tkinter, JSON file I/O, pyperclip |
| `dynamic typing ` | Typing Speed Test | Tkinter, timers, WPM logic |
| `Solution+-+flash-card-project-end` | Flash Cards | Tkinter, pandas, spaced repetition |
| `monady motivation` | Monday Motivation emails | smtplib, datetime |
| `birthday-wisher-extrahard-start` | Birthday Wisher | pandas, SMTP, letter templates |

### Days 31–40 — Working with APIs

| Folder | Project | Concepts practiced |
| --- | --- | --- |
| `kanye-quotes-end` | Kanye Quotes | `requests`, REST APIs, Tkinter |
| `Solution+-+quizzler-app-end` | Quizzler | OpenTrivia API, OOP Tkinter UI |
| `daily umbrella remider ` | Rain Alert | OpenWeatherMap API, Twilio SMS, env vars |
| `stock news fetcher ` | Stock News Alert | Alpha Vantage + News API + Twilio |
| `exercise-tracker` | Exercise Tracker | Nutritionix NLP API + Sheety |
| `recording cycling distance` | Cycling Log | Sheety / Google Sheets API logging |
| `Day-40-Flight-Club` | Flight Club | Tequila flight search API, Sheety, Twilio |

### Days 41–44 — Web foundations (HTML & CSS)

| Folder | Project | Concepts practiced |
| --- | --- | --- |
| `Day-41-Movie-Ranking` | Movie Ranking page | HTML elements, lists |
| `Day-42-Birthday-Invite` | Birthday Invite | HTML structure, images |
| `day-43-colour-vocab` | Colour Vocabulary | CSS selectors |
| `day-44-motivational-poster` | Motivational Poster | CSS box model, fonts |

### Days 45–53 — Web scraping & browser automation (BeautifulSoup + Selenium)

| Folder | Project | Concepts practiced |
| --- | --- | --- |
| `day 46` | Amazon Price Tracker | BeautifulSoup scraping (note: folder is named `day 46` but holds the Day 47 project) |
| `day 47` | Spotify Playlist (musical time machine) | scraping + Spotify API (holds the Day 46 project) |
| `Day48` | Cookie Clicker Bot | Selenium clicking, cookies |
| `Day49` | LinkedIn Bot | Selenium form automation |
| `Day50` | Tinder Bot | Selenium login + swiping |
| `Day51` | Twitter Complaint Bot | Selenium speed test + tweeting |
| `Day52` | Instagram Follower Bot | Selenium find/follow |
| `Day53` | Rental Data Entry bot | scrape Zillow → auto-fill Google Form |

### Days 54–61 — Web apps with Flask

| Folder | Project | Concepts practiced |
| --- | --- | --- |
| `Day55` | Higher-Lower URL Game | Flask routing, URL parsing |
| `Day56` | Name Card site | Flask `static/` + `templates/` |
| `Day57` | Blog (part 1) | Jinja templating |
| `Day58` | TinDog | Bootstrap 5 landing page |
| `Day59` | Blog (Bootstrap theme) | Flask + Bootstrap |
| `Day60` | Blog Contact Form | HTML forms, POST, smtplib |
| `Day61` | Secrets | Flask-WTF, WTForms validation |

---

## Expense Tracker (`app/`)

A full-featured FastAPI application built to practice production-style structure:

- User registration & login with JWT auth (`app/routers/auth.py`)
- Expense CRUD, categories, dashboards & reports (`routers/expenses.py`, `routers/reports.py`)
- Analytics/charts, currency conversion, weather/news/email/AI services (`app/services/`)
- SQLAlchemy models + SQLite (`app/db/`)
- Docker + docker-compose + GitHub Actions CI

### Run it with Docker

```bash
docker compose up --build
```

### Run it locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload   # API docs at http://127.0.0.1:8000/docs
```

### Run the tests

```bash
pytest tests/
```

---

## Running a course project

```bash
cd "<project-folder>"
python main.py
```

Some projects need extra packages (`requests`, `pandas`, `flask`, `selenium`, ...). Check that folder's own imports, or install the shared dependencies:

```bash
pip install -r requirements.txt
```

API-based projects read keys from a `.env` file — copy the folder's `.env.example` and fill in your own keys. Turtle-based games open a GUI window, so they need a desktop environment.

---

## License

[MIT](./LICENSE)
