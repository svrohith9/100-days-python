import requests

res = requests.get(url="http://api.open-notify.org/iss-now.json")

print(res.json())
print(
    f"ISS LAT: {res.json()['iss_position']['latitude']} and LON: {res.json()['iss_position']['longitude']}"
)
