import os

import requests
from dotenv import load_dotenv


load_dotenv()


SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")
SHEETY_SHEET_KEY = os.getenv("SHEETY_SHEET_KEY", "workout")


if not SHEETY_ENDPOINT:
    raise ValueError(
        "SHEETY_ENDPOINT must be set in your .env file."
    )


def save_workout(workout):
    headers = {
        "Content-Type": "application/json",
    }

    if SHEETY_TOKEN:
        headers["Authorization"] = f"Bearer {SHEETY_TOKEN}"

    payload = {
        SHEETY_SHEET_KEY: {
            "date": workout["date"],
            "time": workout["time"],
            "exercise": workout["exercise"],
            "duration": workout["duration"],
            "calories": workout["calories"],
        }
    }

    response = requests.post(
        SHEETY_ENDPOINT,
        json=payload,
        headers=headers,
        timeout=30,
    )

    response.raise_for_status()

    return response.json()
