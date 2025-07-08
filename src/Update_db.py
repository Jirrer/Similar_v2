import sqlite3
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials
import os
import spotipy

load_dotenv()

def parseSong()

def updateDB(songs):
    conn = sqlite3.connect("Spotify_IDs.db")
    cursor = conn.cursor()

    for id, genre in songs.items():
        
        genres = genre.split(',')

        cursor.execute("INSERT INTO song_ids (id, genre) VALUES (?, ?);", (id, str(genres)))

    conn.commit()
    conn.close()






conn = sqlite3.connect("Spotify_IDs.db")
cursor = conn.cursor()

cursor.execute('''
select * from song_ids;
''')

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
