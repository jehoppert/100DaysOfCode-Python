import os
import requests

SHEETY_URL = "https://api.sheety.co/4b53aa58b76af8d63d1933b48fc12423/flightDeals/users"

SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")

print("Welcome to the Flight CLub")
print("We find the best flight deals and email them to you")
first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")
email = input("What is your email?\n")
confirm_email = input("Confirm your email\n")

if email == confirm_email:
    print("You are now in the Flight Club!")

    sheety_headers = {
        "Authorization": f"Basic {SHEETY_TOKEN}"
    }

    sheety_params = {
        "user": {
            "firstName": first_name.title(),
            "lastName": last_name.title(),
            "email": email
        }
    }

    response = requests.post(
        SHEETY_URL, headers=sheety_headers, json=sheety_params)
    response.raise_for_status()

else:
    print("Email does not match, please re-register")
