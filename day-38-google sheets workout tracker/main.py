# https://www.nutritionix.com/business/api
# https://openai.com/blog/openai-api/
# https://sheety.co/

import os
import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 69
HEIGHT_CM = 180
AGE = 28


NUTRITIONIX_APP_ID = os.environ.get("NUTRITION_APP_ID")
NUTRITIONIX_API_KEY = os.environ.get("NUTRITION_API_KEY")

NUTRITIONIX_NLP_EXERCISE_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"

SHEETY_URL = "https://api.sheety.co/4b53aa58b76af8d63d1933b48fc12423/myWorkouts/workouts"

SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")

# natural language process user input for workout information

exercise_text = input("Tell me which exercises you did: ")

nutritionix_npl_exercise_headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
}

nutritionix_npl_exercise_parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(NUTRITIONIX_NLP_EXERCISE_URL, headers=nutritionix_npl_exercise_headers,
                         json=nutritionix_npl_exercise_parameters)
response.raise_for_status()
result = response.json()

# update out google sheet with sheety with the workout info

todays_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

sheety_headers = {
    "Authorization": f"Basic {SHEETY_TOKEN}"
}

for exercise in result["exercises"]:
    sheety_parameters = {
        "workout": {
            "date": todays_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

# could use auth param and pass in username/password for basic auth
# we opt for the base64 encoded "username password" passed as a token
response = requests.post(
    SHEETY_URL, headers=sheety_headers, json=sheety_parameters)
response.raise_for_status()
print(response.text)
