import os
import requests


class DataManager:

    def __init__(self):
        self.sheety_endpoint = os.environ["SHEETY_ENDPOINT"]
        self.username = os.getenv("SHEETY_USERNAME")
        self.password = os.getenv("SHEETY_PASSWORD")

    def get_destination_data(self):
        response = requests.get(
            url=f"{self.sheety_endpoint}/prices",
            auth=(self.username, self.password)
        )

        response.raise_for_status()

        data = response.json()

        return data["prices"]

    def update_destination_codes(self, destination_data):

        for city in destination_data:

            response = requests.put(
                url=f"{self.sheety_endpoint}/prices/{city['id']}",
                json={
                    "price": city
                },
                auth=(self.username, self.password)
            )

            response.raise_for_status()

    def get_customer_emails(self):

        response = requests.get(
            url=f"{self.sheety_endpoint}/users",
            auth=(self.username, self.password)
        )

        response.raise_for_status()

        data = response.json()

        return data["users"]
