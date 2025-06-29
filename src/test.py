import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Authenticate with your credentials
client_id = '9b3f9898efce40ee8dcc3de9907bea84'
client_secret = '5a1e258ec5fb49328527b44554006bc6'
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

# Example track ID (replace with a valid full track ID)
track_id = "0gVni0CzLUorl3ev8zN2gc"

# Get track info
track = sp.track(track_id)

print(f"Track: {track['name']}")

# Loop through all artists on the track
for artist in track['artists']:
    artist_name = artist['name']
    artist_id = artist['id']

    # Get genres for this artist
    artist_info = sp.artist(artist_id)
    genres = artist_info.get('genres', [])[:3]  # Take top 3 genres

    print(f"Artist: {artist_name}")
    print(f"Top Genres: {genres}")
    print('---')
