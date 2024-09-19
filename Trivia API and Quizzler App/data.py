import requests

parameters = {
    "amount": 10,
    "type": "boolean",
}

URL_ENDPOINT = "https://opentdb.com/api.php"

response = requests.get(URL_ENDPOINT, params=parameters)
response.raise_for_status()

data = response.json()
question_data = (data['results'])