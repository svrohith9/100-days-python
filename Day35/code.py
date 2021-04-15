import requests

apikey = {{API_KEY}}
params = {
    "lat": "37.215520",
    "lon": "-93.292360",
    "appid": apikey,
    "exclude": "current,minutely,daily"
}
one_api_call = requests.get(
    url="https://api.openweathermap.org/data/2.5/onecall", params=params)

one_api_call.raise_for_status()
response = one_api_call.json()

weather_ids = [x['weather'][0]["id"] for x in response["hourly"]]
is_umbrella_required = False
for id in weather_ids:
    if int(id) < 700:
        is_umbrella_required = True

if is_umbrella_required:
    print("Bring Umbrella !")
else:
    print("Umbrealla not requried")
