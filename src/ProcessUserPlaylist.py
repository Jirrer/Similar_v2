import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
from itertools import islice
import sys

load_dotenv()

def getSongs(playListID):
    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

    auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(auth_manager=auth_manager)

    all_tracks = []
    offset = 0
    limit = 100

    while True:
        response = sp.playlist_items(playListID, offset=offset, limit=limit)
        items = response.get('items', [])
        all_tracks.extend(items)
        if len(items) < limit:
            break
        offset += limit

    # Return in the same structure as before
    return {'items': all_tracks}

def chunks(iterable, size):
    it = iter(iterable)
    return iter(lambda: list(islice(it, size)), [])

def getGenresAndArtists(songs):
    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

    auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(auth_manager=auth_manager)
    
    artistIDs = []
    genres = []
    foundArtists = []

    for track in songs['items']:
        trackData = track.get('track')

        if not trackData:
            continue

        temp = [a['id'] for a in trackData['artists'][:3]]
        artistIDs.extend(temp)
        foundArtists.append(temp)

    for batch in chunks(artistIDs, 50):  # Spotify limit is 50 per request
        response = sp.artists(batch)
        for artist in response['artists']:
            genres.append(artist.get('genres'))

    return (genres, artistIDs)

def sortGenres(genres):
    values = {}

    for song in genres:
        if not song:
            continue

        for genre in song:
            if genre in values:
                values[genre] += 1
            else:
                values[genre] = 1

    return values

def sortArtists(artists):
    values = {}
    count = 0

    for id in artists:
        count += 1
        if id in values:
            values[id] += 1
        else:
            values[id] = 1

    return values

def getOriginalSongIds(playlistID):
    songs = getSongs(playlistID)
    ids = set()
    for item in songs['items']:
        track = item.get('track')
        if track and track.get('id'):
            ids.add(track['id'])
    return ids

def getOriginalSongsFromData(songs):
    ids = set()
    for item in songs['items']:
        track = item.get('track')
        if track and track.get('id'):
            ids.add(track['id'])
    return ids

def processPlaylist(playlistID):
    songs = getSongs(playlistID)
    genresANDartists = getGenresAndArtists(songs)
    genres = genresANDartists[0]
    artists = genresANDartists[1]
    sortedGenres = sortGenres(genres)
    sortedArtists = sortArtists(artists)
    originalIDs = getOriginalSongsFromData(songs)
    return (sortedGenres, sortedArtists, originalIDs)