import requests

# opentdb.com/api_config.php - trivia question API
ENDPOINT_URL = "https://opentdb.com/api.php"
parameters = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get(url=ENDPOINT_URL, params=parameters)
response.raise_for_status()
data = response.json()

question_data = data["results"]
