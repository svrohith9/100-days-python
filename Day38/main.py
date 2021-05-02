import requests
from datetime import datetime
import os

GENDER = "male"
WEIGHT_KG = "81"
HEIGHT_CM = "171"
AGE = "23"

APP_ID =   # "YOUR APP ID"
API_KEY =   # "YOUR API_KEY"
GENDER =   # YOUR GENDER
WEIGHT_KG =   # YOUR WEIGHT
HEIGHT_CM =   # YOUR HEIGHT
AGE =   # YOUR AGE

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
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
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

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

    # Basic Auth
    sheet_response = requests.post(
        SHEET_ENDPOINT,
        json=sheet_inputs,
        auth=(
            USERNAME,
            PASSWORD
        )
    )

    # Bearer Token
    # bearer_headers = {
    #     "Authorization": f"Bearer {TOKEN}",
    #     "Content-Type": "application/json",
    # }
    # sheet_response = requests.post(
    #     SHEET_ENDPOINT,
    #     json=sheet_inputs,
    #     headers=bearer_headers
    # )

    print(sheet_response.text)
