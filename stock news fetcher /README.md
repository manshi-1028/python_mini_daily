# 📈 Stock News Alert

A Python application that monitors Tesla's stock price and automatically sends the latest news articles via SMS whenever the stock price changes by **5% or more** compared to the previous trading day.

---

## 🚀 Features

* 📊 Fetches daily stock prices using the Alpha Vantage API.
* 📈 Calculates the percentage change between the last two trading days.
* 📰 Retrieves the latest 3 news articles related to Tesla using NewsAPI.
* 📱 Sends each news article as an SMS using Twilio.
* ⚡ Simple and beginner-friendly Python project demonstrating API integration and automation.

---

## 🛠️ Technologies Used

* Python 3
* Requests
* Alpha Vantage API
* NewsAPI
* Twilio SMS API

---

## 📂 Project Structure

```text
stock-news-alert/
│
├── main.py
├── requirements.txt
├── .gitignore
├── README.md
└── .env.example
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/stock-news-alert.git
cd stock-news-alert
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure API Keys

Replace the placeholder values in `main.py` (or use environment variables):

```python
STOCK_API_KEY = "YOUR_ALPHA_VANTAGE_API_KEY"
NEWS_API_KEY = "YOUR_NEWS_API_KEY"

ACCOUNT_SID = "YOUR_TWILIO_ACCOUNT_SID"
AUTH_TOKEN = "YOUR_TWILIO_AUTH_TOKEN"

FROM_NUMBER = "YOUR_TWILIO_PHONE_NUMBER"
TO_NUMBER = "YOUR_PHONE_NUMBER"
```

---

## ▶️ Run the Project

```bash
python main.py
```

---

## 📱 Example SMS

```text
TSLA: 🔺6.25%

Headline: Tesla unveils new AI-powered vehicle features

Brief: Tesla announced several new AI features designed to improve autonomous driving and enhance the user experience.
```

---

## 📌 How It Works

1. Fetches Tesla's daily stock prices from Alpha Vantage.
2. Compares yesterday's closing price with the previous trading day's closing price.
3. Calculates the percentage difference.
4. If the change is **5% or greater**, it fetches the latest three Tesla-related news articles.
5. Sends each article as an SMS using Twilio.

---

## 📦 Requirements

* Python 3.8+
* requests
* twilio

Install all dependencies with:

```bash
pip install -r requirements.txt
```

---

## 🔮 Future Improvements

* Support multiple stock symbols.
* Email notifications.
* Telegram and Discord notifications.
* Schedule automatic execution every day.
* Store stock history in a database.
* Add logging and better error handling.
* Use environment variables for secure API key management.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Developed as part of a Python API and automation learning project to practice working with REST APIs, JSON data, and SMS notifications.
