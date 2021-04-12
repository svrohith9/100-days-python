import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}
question_get_api = requests.get(
    url="https://opentdb.com/api.php", params=parameters)
question_get_api.raise_for_status()
response = question_get_api.json()
question_data = response['results']
