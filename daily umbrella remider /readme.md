# 🌧️ Rain Alert SMS App

A simple Python application that checks the weather forecast using the OpenWeatherMap API and sends an SMS reminder via Twilio if rain is expected within the next few hours.

## ✨ Features

- 🌦️ Fetches weather forecast data from OpenWeatherMap
- ☔ Detects rain based on weather condition codes
- 📱 Sends an SMS notification using Twilio
- 🔐 Uses environment variables for API keys and authentication tokens

## 🛠️ Technologies Used

- Python 3
- Requests
- OpenWeatherMap API
- Twilio API

## 📂 Project Structure

```
rain-alert/
│── main.py
│── README.md
```

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/rain-alert.git
cd rain-alert
```

### 2. Install Dependencies

```bash
pip install requests twilio
```

### 3. Get API Credentials

#### OpenWeatherMap

- Create an account on OpenWeatherMap.
- Generate an API key.

#### Twilio

- Create a Twilio account.
- Get your:
  - Account SID
  - Auth Token
  - Twilio Phone Number
- Verify your personal phone number (required for trial accounts).

### 4. Set Environment Variables

#### Windows (PowerShell)

```powershell
$env:OWM_API_KEY="your_openweathermap_api_key"
$env:AUTH_TOKEN="your_twilio_auth_token"
$env:https_proxy="your_proxy_if_required"
```

#### macOS/Linux

```bash
export OWM_API_KEY="your_openweathermap_api_key"
export AUTH_TOKEN="your_twilio_auth_token"
export https_proxy="your_proxy_if_required"
```

Replace the following placeholders in the code:

```python
account_sid = "YOUR ACCOUNT SID"
from_ = "YOUR TWILIO VIRTUAL NUMBER"
to = "YOUR VERIFIED PHONE NUMBER"
```

## ▶️ Run the Application

```bash
python main.py
```

## 📌 How It Works

1. Sends a request to the OpenWeatherMap Forecast API.
2. Retrieves the next four forecast periods.
3. Checks each weather condition code.
4. If any condition code is below **700** (rain, snow, drizzle, thunderstorms, etc.), it determines that precipitation is expected.
5. Sends an SMS reminder using Twilio.

## 🌦️ Weather Condition Logic

```python
if condition_code < 700:
    will_rain = True
```

Weather condition codes below **700** generally represent:

- Thunderstorm
- Drizzle
- Rain
- Snow
- Atmosphere (mist, fog, etc.)

## 📱 Example SMS

```
It's going to rain today. Remember to bring an ☔️
```

## 🔒 Environment Variables

| Variable | Description |
|----------|-------------|
| `OWM_API_KEY` | OpenWeatherMap API Key |
| `AUTH_TOKEN` | Twilio Auth Token |
| `https_proxy` | HTTPS Proxy (optional, required in some environments) |

## 📄 License

This project is intended for educational purposes and can be modified or extended for personal use.
