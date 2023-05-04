import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()  # Required to load .env

client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
redirect_uri = os.getenv("SPOTIFY_REDIRECT_URI")

# Spotify configs
scope = ['playlist-modify-public', 'user-modify-playback-state']
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                     client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))


def get_tracks_by_genre(genre: str):
    response = sp.search(q=f"""genre:'{genre}'""", type='track')
    tracks_list = []

    if (response):
        for track in response['tracks']['items']:
            tracks_list.append(
                f"{track['name']} by {track['artists'][0]['name']} from the album {track['album']['name']}. Spotify URI: {track['uri']}")

    return tracks_list


def add_track_to_queue(track_uri: str):
    try:
        sp.add_to_queue(track_uri)
        return "Added track to queue successfully"
    except:
        return "Error adding track to queue"


def find_song_by_name(name: str):
    results = sp.search(q=name, type='track')
    if (results):
        song_uri = results['tracks']['items'][0]['uri']
        return song_uri
