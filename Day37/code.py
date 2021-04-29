import requests

pixela_create_user = "https://pixe.la/v1/users"
pixela_username = "svrohith9"
pixela_token = "thisissecret",  # create your custom key here
create_user_params = {
    "token": pixela_token,
    "username": pixela_username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
    "thanksCode": "ThisIsThanksCode"
}

create_user_response = requests.post(
    url=pixela_create_user, json=create_user_params)

print(create_user_response.text)
