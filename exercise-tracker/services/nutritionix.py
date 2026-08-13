import os

import requests
from dotenv import load_dotenv


load_dotenv()


NUTRITIONIX_ENDPOINT = (
    "https://trackapi.nutritionix.com/v2/natural/exercise"
)

APP_ID = os.getenv("NUTRITIONIX_APP_ID")
APP_KEY = os.getenv("NUTRITIONIX_APP_KEY")

if not APP_ID or not APP_KEY:
    raise ValueError(
        "NUTRITIONIX_APP_ID and NUTRITIONIX_APP_KEY "
        "must be set in your .env file."
    )


def get_exercise_data(query):
    headers = {
        "x-app-id": APP_ID,
        "x-app-key": APP_KEY,
        "Content-Type": "application/json",
    }

    data = {
        "query": query,
    }

    response = requests.post(
        NUTRITIONIX_ENDPOINT,
        json=data,
        headers=headers,
        timeout=30,
    )

    response.raise_for_status()

    result = response.json()

    return result.get("exercises", [])
