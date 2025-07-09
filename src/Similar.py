from ProcessUserPlaylist import processPlaylist, getOriginalSongs
from ProccessDB import fetchSongs
import random

newPlaylistLength = 30 # number of new songs
similarityLowLevel = 3.0 # minimum level of similarity 

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


def findSimilars(amount, lst):
    seen = set()
    unique_items = []
    for item in lst:
        if item[0] not in seen:
            unique_items.append(item)
            seen.add(item[0])
    if amount > len(unique_items):
        amount = len(unique_items)
    return random.sample(unique_items, amount)

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

def createNewPlaylist(lst):
    global newPlaylistLength

    lst = lst[0:findCutoff(lst, similarityLowLevel)]


    seen = set()
    unique_lst = []
    for item in lst:
        if item[0] not in seen:
            unique_lst.append(item)
            seen.add(item[0])

    total = len(unique_lst)
    if total < newPlaylistLength:
        raise ValueError("Not enough unique songs to fill the playlist.")
    lst = lst[0:findCutoff(lst, similarityLowLevel)]

    highCount = round(newPlaylistLength * 2 / 3)
    midCount = round(newPlaylistLength / 6)
    lowCount = newPlaylistLength - highCount - midCount  

    high_slice = unique_lst[:highCount]
    mid_slice = unique_lst[highCount:highCount+midCount]
    low_slice = unique_lst[highCount+midCount:highCount+midCount+lowCount]

    highOutput = findSimilars(highCount, high_slice)
    midOutput = findSimilars(midCount, mid_slice)
    lowOutput = findSimilars(lowCount, low_slice)

    result = highOutput + midOutput + lowOutput
    random.shuffle(result)
    return [item[0] for item in result]
    
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
    playlistInfo = processPlaylist('0obEJIDsrmoXkU6Uulwq7F')
    weightedList = createWeightedList(playlistInfo)
    sortedList = sortList(weightedList)
    originalSongs = filterOutOriginals(sortedList, getOriginalSongs('0obEJIDsrmoXkU6Uulwq7F'))
    newPlaylist = createNewPlaylist(originalSongs)

    print(sortedList)

    print(len(newPlaylist))
    for x in newPlaylist:
        print(x)


if __name__ == "__main__":
    main()
