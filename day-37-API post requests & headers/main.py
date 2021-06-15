# https://pixe.la/
# https://docs.pixe.la/

import os
import requests
from datetime import datetime

TOKEN = os.environ.get("PIXELA_TOKEN")
USERNAME = os.environ.get("PIXELA_USERNAME")

# create a user account on Pixela
PIXELA_URL = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(PIXELA_URL, json=user_params)
# print(response.text)

# https://pixe.la/@jehoppert

# create a graph for our account
PIXELA_GRAPH_URL = f"{PIXELA_URL}/{USERNAME}/graphs"

graph_headers = {
    "X-USER-TOKEN": TOKEN
}

graph_params = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "Minutes",
    "type": "int",
    "color": "shibafu"
}

# response = requests.post(url=PIXELA_GRAPH_URL, headers=graph_headers, json=graph_params)
# print(response.text)


# post a pixel to graph
graphID = "graph1"
PIXELA_GRAPH_PIXEL_URL = f"{PIXELA_URL}/{USERNAME}/graphs/{graphID}"

graph_pixel_headers = {
    "X-USER-TOKEN": TOKEN
}

today = datetime.now().strftime("%Y%m%d")

graph_pixel_params = {
    "date": today,
    "quantity": "60",
}

# response = requests.post(url=PIXELA_GRAPH_PIXEL_URL, headers = graph_pixel_headers, json = graph_pixel_params)
# print(response.text)

# put to update a pixel on the graph
PIXELA_GRAPH_UDATE_URL = f"{PIXELA_URL}/{USERNAME}/graphs/{graphID}/{today}"

graph_update_headers = {
    "X-USER-TOKEN": TOKEN
}

graph_update_params = {
    "quantity": "30"
}

#response = requests.put(url=PIXELA_GRAPH_UDATE_URL,headers=graph_update_headers, json=graph_update_params)
# print(response.text)

# delete a pizel on the graph
PIXELA_GRAPH_DELETE_URL = f"{PIXELA_URL}/{USERNAME}/graphs/{graphID}/{today}"

graph_delete_headers = {
    "X-USER-TOKEN": TOKEN
}

#response = requests.delete(url=PIXELA_GRAPH_UDATE_URL,headers=graph_update_headers)
# print(response.text)
