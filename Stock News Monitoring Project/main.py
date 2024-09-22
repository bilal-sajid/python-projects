import requests
import datetime
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "[API KEY]"
NEWS_API_KEY = "[api key]"


### To Get the Stock from API ###
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}
response = requests.get(STOCK_ENDPOINT,params=stock_parameters)
data = response.json()

time_series_data = data["Time Series (Daily)"]

closing_stock_prices = [value["4. close"] for (key, value) in time_series_data.items()]

# Finding the closing prices and the percentage difference
yesterday_stock_price = float(closing_stock_prices[0])
day_before_yesterday_stock_price = float(closing_stock_prices[1])

difference = ((yesterday_stock_price) - (day_before_yesterday_stock_price))

up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"


percentage_difference = round((difference/yesterday_stock_price) * 100)

# Getting related news if the difference was huge
if abs(percentage_difference) > 5:
    # previous_date = datetime.datetime.today() - datetime.timedelta(days=1)
    # previous_date = previous_date.date()
    
    news_parameters = {
        "q": COMPANY_NAME,
        # "from": previous_date,
        "apiKey": NEWS_API_KEY
    }

    # url = f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&from=2024-09-18&sortBy=popularity&apiKey={NEWS_API_KEY}"

    response = requests.get("https://newsapi.org/", params=news_parameters)
    data = response.json()

    articles = data["articles"]

    #Taking the top few articles
    top_3_articles = articles[:3]


    formatted_articles = [f"{STOCK_NAME}:{up_down}{percentage_difference}%\nHeadline: {article['title']}.\nBrief: {article['description']}" for article in top_3_articles]

    
    account_sid = ["TWILIO_ACCOUNT_SID"]
    auth_token = ["TWILIO_AUTH_TOKEN"]

    client = Client(account_sid, auth_token)
    
    for article in formatted_articles:
        message = client.messages.create(
            body= article,
            from_="Twilio Virtual Number",
            to="Actual Number",
        )



