from flask import Flask, request, redirect, session
import spotipy
from spotipy.oauth2 import SpotifyOAuth

app = Flask(__name__)

# Be sure to replace these with your own values
app.secret_key = 'your-secret-key'
app.config["SESSION_COOKIE_NAME"] = 'spotify-login-session'
app.config['SESSION_TYPE'] = 'filesystem'

# Set up spotipy with SpotifyOAuth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='your-spotify-client-id',
    client_secret='your-spotify-client-secret',
    redirect_uri='your-app-redirect-url',
    scope='user-library-read'))

@app.route('/')
def index():
    return 'Welcome to the Spotify Playlist Analyzer!'

@app.route('/login')
def login():
    auth_url = sp.auth_manager.get_authorize_url()
    return redirect(auth_url)

@app.route('/callback')
def callback():
    sp.auth_manager.get_access_token(request.args.get('code'))
    return redirect('analyze')

@app.route('/analyze')
def analyze():
    if not sp.auth_manager.get_access_token():
        return redirect('login')

    # Now you can use `sp` to make requests to the Spotify API
    results = sp.current_user_saved_tracks()
    return f'Found {len(results["items"])} tracks!'

if __name__ == '__main__':
    app.run(debug=True)
