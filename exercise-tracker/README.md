# 🏋️ Exercise Tracker

A Python-based exercise tracking application that uses natural language to
recognize workouts, calculates estimated calories burned, and automatically
stores the results in Google Sheets.

## 🚀 Features

- Enter exercises using natural language
- Detect exercise type automatically
- Calculate exercise duration
- Estimate calories burned
- Automatically save workouts to Google Sheets
- Secure API credentials using environment variables
- Modular Python project structure
- Error handling for failed API requests

---

## 🧠 How It Works

The application follows this flow:

User Input
    ↓
Nutritionix API
    ↓
Exercise Detection
    ↓
Calories + Duration
    ↓
Sheety API
    ↓
Google Sheets

Example input:

"I ran 5 km and cycled for 20 minutes"

The application sends the natural-language query to Nutritionix.

Nutritionix returns information such as:

- Exercise name
- Duration
- Calories burned

The application then saves that information to Google Sheets.

---

## 📁 Project Structure

```text
exercise-tracker/
│
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
├── .env.example
├── .gitignore
│
└── services/
    ├── __init__.py
    ├── nutritionix.py
    └── sheety.py
