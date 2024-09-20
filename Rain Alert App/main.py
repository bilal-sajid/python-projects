import requests
from twilio.rest import Client

API_KEY = "[Key]"
URL_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

account_sid = '[Account]'
auth_token = '[Token]'

weather_params = {
    "lat": 2.769700,#40.712776,
    "lon": 27.618370,#-74.005974,
    "appid": API_KEY,
    "cnt": 4
}

response = requests.get(URL_ENDPOINT, params = weather_params)
response.raise_for_status()
# print(response.status_code)

weather_data = response.json()
# print(weather_data)

will_Rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]

    if int(condition_code) < 700:
        will_Rain = True
        

if will_Rain:
    print("It will rain")
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    from_='sender_number',
    body="It's going to rain today. Bring an Umbrella",
    to='recipient_number'
    )

    print(message.status)
