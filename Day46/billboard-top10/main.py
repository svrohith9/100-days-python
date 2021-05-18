import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

user_input = input("Enter the date YYYY-MM-DD for BillBoard playlist:")

# fetch billboard
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

# OAuth Spotify and fetch
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="YOUR CLIENT ID",
                                               client_secret="YOUR CLIENT SECRET",
                                               redirect_uri="redirect URI",
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path="token.txt"))
# Spotify userid
user_id = sp.current_user()['id']
# print(user_id)

song_uris = []
year = user_input.split("-")[0]

for song in songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    # fetch and append spotify song uris
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


# create a playlist YYYY-MM-DD Billboard 10 and append songs into it

playlist = sp.user_playlist_create(
    user=user_id, name=f"{user_input} Billboard 10", public=False)

# append songs to new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
