from ProcessUserPlaylist import processPlaylist, getOriginalSongs
from ProccessDB import fetchSongs
import random

newPlaylistLength = 30 # number of new songs

def getSongs(genres):
    songs = fetchSongs(genres)

    return songs

def createWeightedList(playlistInfo):
    songsFromDB = getSongs(playlistInfo[0])

    output = [None] * len(songsFromDB)

    userGenres = playlistInfo[0]
    userArtists = playlistInfo[1]

    weight = 0
    count = 0
    for song in songsFromDB:
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
        
def sortList(lst):
    sorted_songs = sorted(lst, key=lambda x: x[1], reverse=True)

    return sorted_songs


def findSimilars(lst, n):
    seen = set()
    count = 0
    output = []

    while count < n and len(seen) != len(lst):
        index = random.randint(0, len(lst) - 1)

        if lst[index][0] not in seen:
            output.append(lst[index])
            seen.add(lst[index][0])
            count += 1

    return output

    

def findCutOff(lst, target):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2

        if lst[mid][1] == target:
            while mid > 0:
                if lst[mid][1] == lst[mid - 1][1]:
                    mid -= 1
                else:
                    return mid

        elif lst[mid][1] < target:
            high = mid - 1
        else:
            low = mid + 1

    return mid

def getAverage(lst):
    count = 0

    for x in lst:
        count += x[1]

    return round(count / len(lst))


def createNewPlaylist(lst):
    global newPlaylistLength

    average = getAverage(lst)


    low = findCutOff(lst, round(average * 0.01))
    mid = findCutOff(lst, round(average * 0.25))
    high = findCutOff(lst, round(average * 0.5))
    
    highSlice = lst[0:high]
    midSlice = lst[high:mid]
    lowSlice = lst[mid:low]

    # for testing it is fixed values
    lowOutput = findSimilars(lowSlice, 5)
    midOutput = findSimilars(midSlice, 5)
    highOutput = findSimilars(highSlice, newPlaylistLength - (len(lowOutput) + len(midOutput)))

    totalOutput = lowOutput + midOutput + highOutput

    if len(totalOutput) < newPlaylistLength:
        temp = findSimilars(lst, newPlaylistLength - len(totalOutput))

        for x in temp:
            totalOutput.append(x)

    random.shuffle(totalOutput)
    return [item[0] for item in totalOutput]

    
def findCutoff(lst, low):
    left = 0
    right = len(lst) - 1

    while (left <= right):
        mid = (left + right) // 2

        if lst[mid][1] <= low:
            right = mid - 1
        else:
            left = mid + 1

    return mid


def filterOutOriginals(candidateList, originalIDs):
    return [item for item in candidateList if item[0] not in originalIDs]

def main():
    playlist = '7y0cXpxR4j1JSJaAvOfyZ0'

    playlistInfo = processPlaylist(playlist)
    weightedList = createWeightedList(playlistInfo)
    sortedList = sortList(weightedList)
    originalIDs = filterOutOriginals(sortedList, getOriginalSongs(playlist))
    newPlaylist = createNewPlaylist(originalIDs)


    for x in newPlaylist:
        print(x)


if __name__ == "__main__":
    main()
