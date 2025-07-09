import sqlite3
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials
import os
import spotipy

load_dotenv()

client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

def getAlbums(artist_id):
    albums = []
    offset = 0
    limit = 50

    while True:
        response = sp.artist_albums(artist_id, album_type="album", limit=limit, offset=offset)
        items = response["items"]
        if not items:
            break
        albums.extend(items)
        offset += limit

    return albums
    


def getArtistSongs(artist_id):
    output = []

    artistAlbum = getAlbums(artist_id)

    for album in artistAlbum:
        albumSongs = sp.album_tracks(album['id'])
        
        for song in albumSongs['items']:
            output.append(song)

    return output



def updateDB(songsArr):
    conn = sqlite3.connect("Spotify_IDs.db")
    cursor = conn.cursor()

    for song in songsArr:
        id = song['id']
        artists = [artist["id"] for artist in song["artists"]]
        genres = [genre for artist_id in artists for genre in sp.artist(artist_id)["genres"]]

        artists_output = ''
        genres_output = ''

        for artist in artists:
            artists_output += artist + ','

        for genre in genres:
            genres_output += genre + ','

        cursor.execute(
            "INSERT OR IGNORE INTO songs (id, genres, artists) VALUES (?, ?, ?);",
            (id, genres_output.rstrip(','), artists_output.rstrip(','))
        )

        print(f"added song {song['name']}")

    conn.commit()
    conn.close()
    print("~~~~~~~~ Committed Additions ~~~~~~~~")



songs = getArtistSongs('6deZN1bslXzeGvOLaLMOIF')
updateDB(songs)




