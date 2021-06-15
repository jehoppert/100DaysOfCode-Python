# https://openweathermap.org/

import os
import requests
from twilio.rest import Client

# create env vars with below in terminal
# to view - env
# to create - export OWM_API_KEY=xxx

# openweathermap constants
ENDPOINT_URL = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = os.environ.get("OWM_API_KEY")
LAT = 57.708870
LON = 11.974560

# twilio constants
ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")

# https://openweathermap.org/api/one-call-api
parameters = {
    "lat": LAT,
    "lon": LON,
    "exclude": "current,minutely,daily",
    "appid": API_KEY
}

response = requests.get(ENDPOINT_URL, params=parameters)
response.raise_for_status()
weather_data = response.json()
hourly_data = weather_data["hourly"][:12]

will_rain = False
hourly_codes = []
for hour in hourly_data:
    if int(hour['weather'][0]['id']) < 700:
        will_rain = True

if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    message = client.messages \
        .create(
            body="Bring an umbrella ☔️",
            from_="+xxxxxxxx",  # twilio account phone number
            to="+xxxxxxxxxx"  # attached account phone number
        )

    print(message.status)
