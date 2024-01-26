import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client
load_dotenv("../.env")
MY_LAT = 56.130367
MY_LONG = -106.346771
API_KEY = os.environ["OPEN_WEATHER_API"]

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "cnt": 4
}
response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params= parameters)
response.raise_for_status()
data = response.json()

will_rain = False
for hour_data in data["list"]:
    condition_code = (hour_data["weather"][0]["id"])
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
                              from_='FROM_NUMBER',
                              body='Hi there',
                              to='TO_NUMBER'
                          )
    print(message.status)     