import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "YOUR_ALPHA_VANTAGE_API_KEY"
NEWS_API_KEY = "YOUR_NEWS_API_KEY"

ACCOUNT_SID = "YOUR_TWILIO_ACCOUNT_SID"
AUTH_TOKEN = "YOUR_TWILIO_AUTH_TOKEN"

FROM_NUMBER = "YOUR_TWILIO_PHONE_NUMBER"
TO_NUMBER = "YOUR_PHONE_NUMBER"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()

data = response.json()["Time Series (Daily)"]
data_list = [value for value in data.values()]

yesterday_closing_price = float(data_list[0]["4. close"])
before_yesterday_closing_price = float(data_list[1]["4. close"])

difference = yesterday_closing_price - before_yesterday_closing_price
difference_percentage = abs(difference) / before_yesterday_closing_price * 100

arrow = "🔺" if difference > 0 else "🔻"

if difference_percentage >= 5:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()

    articles = news_response.json()["articles"][:3]

    formatted_articles = [
        f"""{STOCK}: {arrow}{difference_percentage:.2f}%
Headline: {article['title']}
Brief: {article['description']}"""
        for article in articles
    ]

    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=FROM_NUMBER,
            to=TO_NUMBER,
        )
        print(message.sid)
