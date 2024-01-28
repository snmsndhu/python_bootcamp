#Habit Tracker

import requests
import os
from dotenv import load_dotenv
load_dotenv("../../.env")
TOKEN = os.environ["TOKEN"]
USER = os.environ["USER_NAME"]
GRAPH_ID = "graph1"


pixel_endpoint = "https://pixe.la/v1/users"

user_params ={
    "token": TOKEN,
    "username": USER,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url = pixel_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixel_endpoint}/{USER}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url = graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixel_endpoint}/{USER}/graphs/{GRAPH_ID}"
pixe_data = {
    "date": "20240128",
    "quantity": "7.70"
}

response = requests.post(url= pixel_creation_endpoint, json=pixe_data, headers=headers)
print(response.text)