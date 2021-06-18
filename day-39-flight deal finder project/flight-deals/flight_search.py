import os
import requests
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = os.environ.get("TEQUILA_API_KEY")


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def __init__(self):
        pass

    def get_destination_code(self, city_name):

        tequila_loc_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"

        tequila_headers = {
            "apikey": TEQUILA_API_KEY
        }

        tequila_params = {
            "term": city_name,
            "location_types": "city"
        }

        response = requests.get(tequila_loc_endpoint,
                                headers=tequila_headers, params=tequila_params)
        response.raise_for_status()

        results = response.json()["locations"]
        code = results[0]['code']
        return code

    def flight_search(self, from_city_code, to_city_code, from_date, to_date):

        tequila_search_endpoint = f"{TEQUILA_ENDPOINT}/v2/search"

        tequila_headers = {
            "apikey": TEQUILA_API_KEY
        }

        tequila_params = {
            "fly_from": from_city_code,
            "fly_to": to_city_code,
            "date_from": from_date.strftime("%d/%m/%Y"),
            "date_to": to_date.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        response = requests.get(tequila_search_endpoint,
                                headers=tequila_headers, params=tequila_params)

        try:
            data = response.json()['data'][0]
        except IndexError:
            print(f"No flights found for {to_city_code}")
            return None

        flight_data = FlightData(
            price=data['price'],
            from_city=data['route'][0]['cityFrom'],
            from_airport=data["route"][0]["flyFrom"],
            to_city=data["route"][0]["cityTo"],
            to_airport=data["route"][0]["flyTo"],
            leave_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )

        print(f"{flight_data.to_city}: £{flight_data.price}")
        return flight_data
