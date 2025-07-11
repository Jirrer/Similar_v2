import random
weightedList = None

def genreAndArtist(userPlaylist, pulledSongs):
    global weightedList

    weightedList = [None] * len(pulledSongs)

    userGenres = userPlaylist[0]
    userArtists = userPlaylist[1]

    weight = 0
    ouptutIndex = 0
    for song in pulledSongs:
        songGenres = song[1].split(',')
        songArtist = song[2].split(',')

        for genre in songGenres:
            if genre in userGenres:
                weight += userGenres[genre]

        for artist in songArtist:
            if artist in userArtists:
                weight += userArtists[artist]

        weightedList[ouptutIndex] = [song[0], weight]
        ouptutIndex += 1
        weight = 0

def getTone(lst): # returns 0 to 100 range of energy
    output = {key: None for key in lst}

    for songId, tone in output.items():
        tone = random.randint(1,99)
        output[songId] = tone

    return output

def getAverageTone(t):
    total = 0

    for x in t.values():
        total += x

    return round(total / len(t))

def getAverageWeight():
    global weightedList

    total = 0
    for x in weightedList:
        total += x[1]

    return round(total / len(weightedList))


#check time of songs too

def checkTone(userIds):
    global weightedList 

    userTone = getTone(userIds)
    pulledDataTone = getTone(x[0] for x in weightedList)

    averageTone = getAverageTone(userTone)

    for song in weightedList:
        difference = abs(averageTone - pulledDataTone[song[0]])
        valueToSubtract = (getAverageWeight() * (difference / 100))
        song[1] -= round(valueToSubtract)
    

def createWeightedList(userPlaylist, pulledSongs):
    global weightedList

    genreAndArtist(userPlaylist, pulledSongs) # weighted list by number of shared gernes and artist
    checkTone(userPlaylist[2])
    
    return [tuple(inner) for inner in weightedList]
