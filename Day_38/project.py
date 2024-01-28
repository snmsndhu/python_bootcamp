#Exercise Tracking with Python and Google sheets

import requests
import os
from dotenv import load_dotenv
load_dotenv("../.env")
from datetime import datetime

ID = os.environ["APP_ID"]
KEY = os.environ["API_KEY"]

GENDER = "Male"
WEIGHT_KG = 70  
HEIGHT_CM = 155
AGE = 20

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = ""

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": ID,
    "x-app-key": KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
bearer_headers = {
"Authorization": "Bearer YOUR_TOKEN"
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=bearer_headers)

    print(sheet_response.text)