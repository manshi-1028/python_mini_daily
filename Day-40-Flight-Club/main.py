from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "LON"

flight_search = FlightSearch()
data_manager = DataManager()
notification_manager = NotificationManager()

# Get destination data from the spreadsheet
sheet_data = data_manager.get_destination_data()

# Add IATA codes to destinations that don't have one
for city in sheet_data:
    if city["iataCode"] == "":
        city["iataCode"] = flight_search.get_destination_code(city["city"])

# Update the spreadsheet with the IATA codes
data_manager.update_destination_codes(sheet_data)

# Search for flights to every destination
for destination in sheet_data:
    flight = flight_search.find_best_flight(
        ORIGIN_CITY_IATA,
        destination["iataCode"]
    )

    if flight:
        # Get all registered customers
        users = data_manager.get_customer_emails()

        # Extract their email addresses
        emails = [user["email"] for user in users]

        # Send the flight deal to all customers
        notification_manager.send_emails(
            emails,
            flight
        )
