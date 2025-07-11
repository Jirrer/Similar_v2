




def createWeightedList(userPlaylist, pulledSongs):
    output = [None] * len(pulledSongs)

    userGenres = userPlaylist[0]
    userArtists = userPlaylist[1]

    weight = 0
    count = 0
    for song in pulledSongs:
        songGenres = song[1].split(',')
        songArtist = song[2].split(',')

        for genre in songGenres:
            if genre in userGenres:
                weight += userGenres[genre]

        for artist in songArtist:
            if artist in userArtists:
                weight += userArtists[artist]

        output[count] = (song[0], weight)
        count += 1
        weight = 0

    return output