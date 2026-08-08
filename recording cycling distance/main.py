import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("PIXELA_TOKEN")
USERNAME = os.getenv("PIXELA_USERNAME")
GRAPH_ID = os.getenv("PIXELA_GRAPH_ID")

BASE_URL = "https://pixe.la/v1/users"

if not TOKEN or not USERNAME or not GRAPH_ID:
    print("❌ Missing Pixela configuration.")
    print("Please check your .env file.")
    exit()

def get_distance():
    while True:
        try:
            distance = float(input("🚴 Enter today's cycling distance (km): "))

            if distance <= 0:
                print("❌ Distance must be greater than 0.")
                continue

            return distance

        except ValueError:
            print("❌ Please enter a valid number.")


def record_cycling(distance):
    today = datetime.now().strftime("%Y%m%d")

    url = f"{BASE_URL}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

    headers = {
        "X-USER-TOKEN": TOKEN
    }

    data = {
        "quantity": f"{distance:.2f}"
    }

    try:
        response = requests.put(
            url=url,
            json=data,
            headers=headers,
            timeout=10
        )

        if response.status_code == 200:
            return True, response.json()

        if response.status_code == 404:
            return False, "User, graph, or token was not found."

        if response.status_code == 400:
            return False, response.json().get("message", "Invalid request.")

        if response.status_code == 409:
            return False, "A pixel conflict occurred."

        return False, f"Pixela returned HTTP {response.status_code}: {response.text}"

    except requests.exceptions.Timeout:
        return False, "Request timed out. Check your internet connection."

    except requests.exceptions.ConnectionError:
        return False, "Could not connect to Pixela."

    except requests.exceptions.RequestException as error:
        return False, f"Request failed: {error}"


def main():
    print()
    print("=" * 40)
    print("        🚴 PIXELA CYCLING TRACKER")
    print("=" * 40)
    print()

    distance = get_distance()

    print()
    print(f"📏 Distance: {distance:.2f} km")
    print(f"📅 Date: {datetime.now().strftime('%d-%m-%Y')}")
    print()
    print("📡 Updating Pixela...")

    success, result = record_cycling(distance)

    if success:
        print()
        print("✅ Successfully recorded!")
        print(f"🚴 {distance:.2f} km added to your cycling graph.")
        print()

    else:
        print()
        print("❌ Failed to record cycling data.")
        print(f"Reason: {result}")
        print()


if __name__ == "__main__":
    main()
