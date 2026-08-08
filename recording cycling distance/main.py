import os
import requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

TOKEN = os.getenv("PIXELA_TOKEN")
USER_NAME = os.getenv("PIXELA_USERNAME")
GRAPH_ID = os.getenv("PIXELA_GRAPH_ID")

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

headers = {
    "X-USER-TOKEN": TOKEN
}

today = datetime.now().strftime("%Y%m%d")

pixel_url = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs/{GRAPH_ID}"

pixel_data = {
    "date": today,
    "quantity": "9.04"
}

response = requests.post(
    url=pixel_url,
    json=pixel_data,
    headers=headers
)

print(response.status_code)
print(response.text)
