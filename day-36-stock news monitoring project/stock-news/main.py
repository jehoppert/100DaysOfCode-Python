# alphavantage.co
# newsapi.org
# twilio.com

import os
import requests
from twilio.rest import Client


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_ENDPOINT = "https://www.alphavantage.co/query"
NEWSAPI_ENDPOINT = "https://newsapi.org/v2/everything"
ALPHA_API_KEY = os.environ.get("ALPHA_API_KEY")
NEWSAPI_API_KEY = os.environ.get("NEWSAPI_API_KEY")

TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")

# check for 5% swiing is stock price between recent two day close

alpha_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHA_API_KEY
}

alpha_response = requests.get(ALPHA_ENDPOINT, params=alpha_parameters)
alpha_response.raise_for_status()
alpha_data = alpha_response.json()['Time Series (Daily)']

# get the recent two days
alpha_data_list = [value for (key, value) in alpha_data.items()][:2]


# closing price yesterday
yesterday_close = float(alpha_data_list[0]['4. close'])
# day before yesterday
day_before_close = float(alpha_data_list[1]['4. close'])

move_percent = "{:.2f}".format(
    (yesterday_close - day_before_close) / day_before_close * 100)

# check if we had a 5% move up or down
if abs(float(move_percent)) > 5:

    # get the news related to the stock after we have confirmed the price movement

    newsapi_parameters = {
        "qInTitle": COMPANY_NAME,
        "pageSize": 3,
        "apiKey": NEWSAPI_API_KEY
    }

    newsapi_response = requests.get(
        NEWSAPI_ENDPOINT, params=newsapi_parameters)
    newsapi_response.raise_for_status()
    newsapi_data = newsapi_response.json()['articles']

    msg = f"{STOCK}: {move_percent}%\n"
    for article in newsapi_data:
        msg += f"{article['title']}\n"

    # send message with twililo to alert

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    message = client.messages \
        .create(
            body=msg,
            from_="+xxxxxxxx",  # twilio account phone number
            to="+xxxxxxxxxx"  # attached account phone number
        )

    print(message.status)
