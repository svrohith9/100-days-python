import requests
from datetime import datetime


def fetch_date():
    today = datetime.now()
    return today.strftime("%Y%m%d")


pixela_create_user = "https://pixe.la/v1/users"
pixela_username = "svrohith9"
pixela_token = "thisisisecret"  # create your custom key here
pixela_graph = "first"
create_user_params = {
    "token": pixela_token,
    "username": pixela_username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
    "thanksCode": "ThisIsThanksCode"
}

# create_user_response = requests.post(
#     url=pixela_create_user, json=create_user_params)

# print(create_user_response.text)

create_graph = f"{pixela_create_user}/{pixela_username}/graphs"
graph_config_params = {
    "id": pixela_graph,
    "name": "Study",
    "unit": "Hrs",
    "type": "float",
    "color": "sora"
}
headers = {
    "X-USER-TOKEN": pixela_token
}

response = requests.post(url=create_graph, json=graph_config_params,
                         headers=headers)
print(response.text)


graph_pixel_url = f"{pixela_create_user}/{pixela_username}/graphs/{pixela_graph}"
current_date = fetch_date()
graph_pixel_config_params = {
    "date": current_date,
    "quantity": "5",
}

graph_pixel_response = requests.post(
    url=graph_pixel_url, json=graph_pixel_config_params, headers=headers)

print(graph_pixel_response.text)
