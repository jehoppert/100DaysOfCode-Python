import requests
from datetime import datetime

# simple get API
# http://open-notify.org/Open-Notify-API/ISS-Location-Now/
ENDPOINT_URL = "http://api.open-notify.org/iss-now.json"

response = requests.get(url=ENDPOINT_URL)
response.raise_for_status()  # non 200 code exception

data = response.json()
longitude = data['iss_position']['longitude']
latitude = data['iss_position']['latitude']

iss_position = (longitude, latitude)
print(iss_position)

# parameter API
# https://sunrise-sunset.org/api

ENDPOINT_URL = "https://api.sunrise-sunset.org/json"
parameters = {
    "lat": 51.507351,
    "lng": -0.127758,
    "formatted": 0
}

# https://api.sunrise-sunset.org/json?lat=51.507351&lng=-0.127758
response = requests.get(url=ENDPOINT_URL, params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now.hour)
