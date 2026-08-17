import os
from datetime import datetime, timedelta

from amadeus import Client, ResponseError


class FlightSearch:

    def __init__(self):

        self.amadeus = Client(
            client_id=os.environ["AMADEUS_API_KEY"],
            client_secret=os.environ["AMADEUS_API_SECRET"]
        )

    def get_destination_code(self, city_name):

        try:

            response = self.amadeus.reference_data.locations.get(
                keyword=city_name,
                subType="CITY"
            )

            return response.data[0]["iataCode"]

        except (ResponseError, IndexError):

            return ""

    def find_best_flight(
            self,
            origin_city_iata,
            destination_city_iata
    ):

        tomorrow = datetime.now() + timedelta(days=1)

        try:

            response = self.amadeus.shopping.flight_offers_search.get(
                originLocationCode=origin_city_iata,
                destinationLocationCode=destination_city_iata,
                departureDate=tomorrow.strftime("%Y-%m-%d"),
                adults=1,
                currencyCode="GBP",
                max=10
            )

            if response.data:

                offer = response.data[0]

                itinerary = offer["itineraries"][0]
                segments = itinerary["segments"]

                return {
                    "price": offer["price"]["total"],
                    "origin": segments[0]["departure"]["iataCode"],
                    "destination": segments[-1]["arrival"]["iataCode"],
                    "departure": segments[0]["departure"]["at"],
                    "arrival": segments[-1]["arrival"]["at"],
                    "stops": len(segments) - 1
                }

        except ResponseError as error:

            print(f"Amadeus API error: {error}")

        return None
