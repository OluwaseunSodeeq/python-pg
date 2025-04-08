import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Declaring needed Variables
Spotify_username = "MY_USERNAME"
year = input("What year would you like to travel to in YY-MM-DD? ")
URL = f"https://www.billboard.com/charts/hot-100/{year}"
CLIENT_ID = "SPOTIFY_CLIENT_ID"
CLIENT_SECRET = "SPOTIFY_CLIENT_SECRET"
Redirect_URL = "https://example.com/"
scope = "playlist-read-private, " \
        "user-read-currently-playing, " \
        "user-read-currently-playing, " \
        "user-follow-read, playlist-modify-private"


# SCRAPING BILLBOARD TOP 100 CHARTS WITH BEAUTIFUL SOUP
response = requests.get(URL)
billboard_website = response.text
soup = BeautifulSoup(billboard_website, "html.parser")
top100 = soup.find_all("h3", class_="u-max-width-330")

# Authenticating Spotify client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=Redirect_URL,
    scope=scope)
)

song_uris = []
for song in top100:
    song_name = song.getText().strip()
    result = sp.search(q=song_name, type="track")

    if result["tracks"]["items"]:
        song_uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(song_uri)
    else:
        print(f"Song {song_name} not found on Spotify")

# Creating a new playlist on Spotify
playlist_name = f"Billboard Hot 100 - {year}"
description = "Top 100 songs on Billboard charts for the specified year."

playlist = sp.user_playlist_create(user=_,
                                   name=playlist_name,
                                   description=description,
                                   public=False)
# Adding songs to playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

# ================================================


# from datetime import datetime
# import requests

# from bs4 import BeautifulSoup


# def get_endpoint(date):
#     while not bool(datetime.strptime(date, "%Y-%m-%d")):
#         print("Sorry, your input did not match the format YYYY-MM-DD, please try again...")
#         date = input(f"Which year do you want to travel? Type the date in this format YYYY-MM-DD: ")

#     return f"https://www.billboard.com/charts/hot-100/{date}/"


# user_input = input("Which year do you want to travel? Type the date in this format YYYY-MM-DD: ")
# endpoint = get_endpoint(date=user_input)
# response = requests.get(endpoint)
# soup = BeautifulSoup(response.text, 'html.parser')
# songs = soup.select("div ul li ul li h3")
# artists = [song.find_next_sibling() for song in songs]

# songs_titles = [song.getText().strip() for song in songs]
# artists_titles = [artist.getText().strip() for artist in artists]

# top_100 = list(zip(artists_titles, songs_titles))

# print(top_100)