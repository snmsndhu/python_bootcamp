#Habit Tracker

import requests
import os
from dotenv import load_dotenv
load_dotenv("../../.env")
TOKEN = os.environ["TOKEN"]
USER = os.environ["USER_NAME"]


pixel_endpoint = "https://pixe.la/v1/users"

user_params ={
    "token": TOKEN,
    "username": USER,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url = pixel_endpoint, json=user_params)
print(response.text)