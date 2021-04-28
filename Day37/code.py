import requests

pixela_create_user = "https://pixe.la/v1/users"

create_user_params = {
    "token": "thisissecret",  # create your custom key here
    "username": "svrohith9",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
    "thanksCode": "ThisIsThanksCode"
}

create_user_response = requests.post(
    url=pixela_create_user, json=create_user_params)

print(create_user_response.text)
