import requests
from bs4 import BeautifulSoup

user_input = input("Enter the date YYYY-MM-DD for BillBoard playlist:")

# Get call billboard
response = requests.get(
    url=f"https://www.billboard.com/charts/hot-100/{user_input}")

response.raise_for_status()

# parse and extract 100 songs
soup = BeautifulSoup(response.text, "html.parser")
span_songs = soup.findAll(
    "span", class_="chart-element__information__song text--truncate color--primary")

# List top 10 songs from span_songs
songs = [song.getText() for song in span_songs[0:10]]
print(songs)
