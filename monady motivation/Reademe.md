# 📧 Monday Motivational Quote Emailer

A simple Python automation project that sends a random motivational quote via email every Monday.

## 🚀 Features

- Reads motivational quotes from a `quotes.txt` file.
- Randomly selects one quote every Monday.
- Sends the quote via Gmail using Python's `smtplib`.
- Uses Python's `datetime` module to check the current day.
- Easy to customize with your own quotes and recipient email.

## 🛠️ Technologies Used

- Python 3
- smtplib
- datetime
- random

## 📂 Project Structure

```
.
├── main.py
├── quotes.txt
└── README.md
```

## ⚙️ Setup

1. Clone the repository.

```bash
git clone https://github.com/your-username/monday-motivational-emailer.git
cd monday-motivational-emailer
```

2. Install Python (3.8+).

3. Replace the following in `main.py`:

```python
my_email = "your_email@gmail.com"
password = "your_app_password"
```

> **Note:** If you're using Gmail, use a Google **App Password** instead of your normal account password.

4. Add your favorite quotes to `quotes.txt` (one quote per line).

5. Run the program:

```bash
python main.py
```

## 📧 Example Email

**Subject**

```
Quote of the Day
```

**Body**

```
Success is the sum of small efforts, repeated day in and day out.
```

## 💡 Future Improvements

- Schedule automatically using GitHub Actions or Cron Jobs.
- Support multiple recipients.
- Read quotes from an online API.
- Add HTML email formatting.
- Track sent quotes to avoid repetition.

## 📜 License

This project is created for learning purposes as part of the **100 Days of Code - Python Bootcamp**.
