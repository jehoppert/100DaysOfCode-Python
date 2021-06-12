import requests
from datetime import datetime
import smtplib
import config


MY_LAT = 57.708870
MY_LONG = 11.974560

ISS_ENDPOINT = "http://api.open-notify.org/iss-now.json"
SUN_ENDPOINT = "https://api.sunrise-sunset.org/json"


def is_ISS_overhead():
    response = requests.get(url=ISS_ENDPOINT)
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # check if position is within +5 or -5 degrees of the ISS position
    if abs(MY_LAT - iss_latitude) < 5 and abs(MY_LONG - iss_longitude) < 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get(url=SUN_ENDPOINT, params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time = datetime.now()

    # is it currently night
    if not sunrise <= time.hour <= sunset:
        return True


if is_ISS_overhead() and is_night():
    # send email notification if ISS is near and its nighttime
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()  # secure encrypted connection
        connection.login(user=config.FROM_EMAIL, password=config.PASSWORD)
        connection.sendmail(from_addr=config.FROM_EMAIL,
                            to_addrs=config.TO_EMAIL, msg=f"Subject:ISS OVERHEAD\n\nLOOK UP")
