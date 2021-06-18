# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

# https://sheety.co/
# https://partners.kiwi.com/
# https://tequila.kiwi.com/portal/docs/tequila_api
# https://www.twilio.com/docs/sms

from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

FROM_CITY_IATA = "LON"

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_destination_data()

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

    if flight is None:
        continue

    if flight.price < row["lowestPrice"]:

        users = data_manager.get_customer_emails()
        emails = [row['email'] for row in users]
        names = [row['firstName'] for row in users]

        message = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}"

        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."

        link = f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}.{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"

        notification_manager.send_emails(emails, message, link)
