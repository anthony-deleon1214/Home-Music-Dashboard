# Importing required packages
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv('.env')     # Loading client ID and secret from .env file

scope = "user-read-playback-state, user-modify-playback-state"     # Setting scope to allow app to control playback of music

sp = spotipy.Spotify(client_credentials_manager=SpotifyOAuth(scope=scope))

devices = sp.devices()
print(devices)
for item in devices['devices']:
    if item['type'] == 'Computer':
        desktop_id = item['id']
    elif item['type'] == 'TV':
        tv_id = item['id']
    elif item['type'] == 'Smartphone':
        phone_id = item['id']

result = sp.search('Festival Grrrl')
track_uri = result['tracks']['items'][0]['uri']
sp.start_playback(device_id=desktop_id, uris=[track_uri])