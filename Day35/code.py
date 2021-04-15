import requests

apikey = "b6af18726beeddb3570ceacf41e8e0ab"
params = {
    "lat": "17.385044",
    "lon": "78.486671",
    "appid": apikey
}
one_api_call = requests.get(
    url="https://api.openweathermap.org/data/2.5/onecall", params=params)

one_api_call.raise_for_status()
response = one_api_call.json()
print(response)
