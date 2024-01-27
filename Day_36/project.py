###Stock News Monitoring Project###
import os
import requests
from dotenv import load_dotenv
load_dotenv("../.env")
STOCK_API_KEY = os.environ["STOCK_PRICE_API"]
NEWS_API_KEY = os.environ["NEW_API_KEY"]

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

new_params = {
    "apiKey": NEWS_API_KEY,
    "qInTitle": COMPANY_NAME,
}

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


response = requests.get(STOCK_ENDPOINT, stock_parameters)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
print(difference)

diff_percent = (difference / float(yesterday_closing_price)) * 100
print(diff_percent)

if diff_percent > 0.1:
    news_response = requests.get(NEWS_ENDPOINT, new_params)
    artical = news_response.json()["articles"]
    three_articals = artical[:3]
    print(three_articals)

    formatted_articles = [f"Headline: {article['title']}, \nBrief: {article['description']}" for article in three_articals]

    print(formatted_articles)