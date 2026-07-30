# 🧠 Quizler App

A simple Python quiz application built using **Tkinter**. The app presents True/False questions, keeps track of the user's score, and provides instant feedback after each answer.

## 📌 Features

- Interactive GUI built with Tkinter
- True/False quiz questions
- Live score tracking
- Instant answer feedback
- Automatically moves to the next question
- Displays final score when the quiz is completed

---

## 📂 Project Structure

```
quizler-app-end/
│
├── images/              # UI assets (icons/images)
├── __pycache__/         # Python cache files
├── data.py              # Stores quiz question data
├── main.py              # Application entry point
├── question_model.py    # Question class/model
├── quiz_brain.py        # Quiz logic and score handling
└── ui.py                # Tkinter user interface
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository

```bash
git clone https://github.com/your-username/quizler-app.git
```

2. Navigate to the project folder

```bash
cd quizler-app-end
```

3. Run the application

```bash
python main.py
```

---

## 🛠 Technologies Used

- Python
- Tkinter

---

## 📖 How It Works

1. The application loads quiz questions from `data.py`.
2. `question_model.py` creates question objects.
3. `quiz_brain.py` manages quiz flow and score.
4. `ui.py` displays the interface and handles user interaction.
5. `main.py` starts the application.

---

## 📸 Preview

Add a screenshot of your application here.

```
![Quiz App Screenshot](images/screenshot.png)
```

---

## 🎯 Learning Objectives

This project demonstrates:

- Object-Oriented Programming (OOP)
- Python classes and modules
- GUI development with Tkinter
- Event-driven programming
- Separation of logic and UI

---

## 👨‍💻 Author

**Manshi**

Built as part of the **100 Days of Code: The Complete Python Pro Bootcamp**.
