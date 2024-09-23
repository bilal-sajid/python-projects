import requests
from datetime import datetime

APP_ID = "<App ID>"
API_KEY = "<Key>"

AGE = 23
GENDER = "male"

sheety_endpoint = "<Endpoint>"

nutrition_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutrition_header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}


exercise_text = input("Query: ")

nutrition_parameters = {
    "query": exercise_text,
    "age": AGE,
    "gender": GENDER,
}

sheety_authorization_header = {
    "Authorization": "Basic QWhtYWQgQmlsYWwgU2FqaWQ6b2Fsc3hhbXBhcG9t"
}

            
response = requests.post(url = nutrition_endpoint, json=nutrition_parameters, headers=nutrition_header)
result = response.json()
# print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheety_endpoint, json=sheet_inputs, headers=sheety_authorization_header)
    # print(sheet_response.text)