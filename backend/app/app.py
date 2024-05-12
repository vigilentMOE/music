from flask import Flask, request, redirect, session
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv('../env.env')

app.secret_key = os.getenv('SPOTIFY_SECRET')
spotify_id: str = os.getenv('SPOTIFY_ID')
redirect_uri_env: str = os.getenv('REDIRECT_URL')
app.config["SESSION_COOKIE_NAME"] = 'spotify-login-session'
app.config['SESSION_TYPE'] = 'filesystem'

# Set up spotipy with SpotifyOAuth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=spotify_id,
    client_secret=app.secret_key,
    redirect_uri=redirect_uri_env,
    scope='user-library-read'))

@app.route('/')
def index():
    return 'Welcome to the Spotify Playlist Analyzer!'

@app.route('/login')
def login():
    auth_url = sp.auth_manager.get_authorize_url()
    return redirect(auth_url)

# Spotify returning auth code  
@app.route('/callback')
def callback():
    # Now get the access token
    sp.auth_manager.get_access_token(request.args.get('code'))
    return redirect('analyze')

# Use the auth code to get stuff
@app.route('/analyze')
def analyze():
    if not sp.auth_manager.get_access_token():
        return redirect('login')

    # Now you can use `sp` to make requests to the Spotify API
    results = sp.current_user_saved_tracks(limit=50)
    user_id = sp.current_user()['id']
    more_results = sp.user_playlists(user=user_id, limit=50)
    return f'Found {len(results["items"])} tracks! \n {more_results}'

if __name__ == '__main__':
    app.run(debug=True, port=8081)
    
