import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"
USERNAME = "your_spotify_username"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username=USERNAME,
    )
)
user_id = sp.current_user()["id"]
travel_date = input("What date would you like to travel to? Write it in YYYY-MM-DD format: ")
URL = f"https://www.billboard.com/charts/hot-100/{travel_date}"
response = requests.get(URL)

webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")
songs = soup.select("div.o-chart-results-list-row-container ul li h3")
song_titles = [song.getText().strip("\n \t") for song in songs]


song_uris = []
year = travel_date.split("-")[0]
for song in song_titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    
    try:
        uri= result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user = user_id, name=f"{travel_date} Billboard 100", public = False)
print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)