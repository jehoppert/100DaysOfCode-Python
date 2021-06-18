# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

# https://sheety.co/
# https://partners.kiwi.com/
# https://tequila.kiwi.com/portal/docs/tequila_api
# https://www.twilio.com/docs/sms

from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()

FROM_CITY_IATA = "LON"

update_required = False
for row in sheet_data:
    if row['iataCode'] == "":
        update_required = True
        row['iataCode'] = flight_search.get_destination_code(
            row['city'])

data_manager.destination_data = sheet_data

if update_required:
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_tday = datetime.now() + timedelta(days=(6*30))

for row in sheet_data:
    flight = flight_search.flight_search(
        FROM_CITY_IATA, row['iataCode'], from_date=tomorrow, to_date=six_month_from_tday)

    if flight.price < row["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}")
