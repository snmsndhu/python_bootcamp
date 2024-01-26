import requests
import os
from dotenv import load_dotenv
load_dotenv("../.env")
MY_LAT = 56.130367
MY_LONG = -106.346771
API_KEY = os.environ["OPEN_WEATHER_API"]

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY
}
response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params= parameters)
print(response.status_code)
data = response.json()
print(data)