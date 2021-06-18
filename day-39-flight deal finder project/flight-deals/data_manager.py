import os
import requests

SHEETY_URL = "https://api.sheety.co/4b53aa58b76af8d63d1933b48fc12423/flightDeals/prices"

SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):

        sheety_headers = {
            "Authorization": f"Basic {SHEETY_TOKEN}"
        }

        response = requests.get(SHEETY_URL, headers=sheety_headers)
        response.raise_for_status()

        # list of dict city objects
        self.destination_data = response.json()["prices"]

        return self.destination_data

    def update_destination_codes(self):
        for row in self.destination_data:

            sheety_headers = {
                "Authorization": f"Basic {SHEETY_TOKEN}"
            }

            sheety_params = {
                "price": {
                    "iataCode": row['iataCode']
                }
            }

            response = requests.put(
                f"{SHEETY_URL}/{row['id']}", headers=sheety_headers, json=sheety_params)
            response.raise_for_status()
