from ProcessUserPlaylist import processPlaylist, getOriginalSongIds
from ProccessDB import fetchSongs
from ProcessPulledData import createWeightedList
import random

newPlaylistLength = 30 # number of new songs

def getSongs(genres):
    songs = fetchSongs(genres)

    return songs

        
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
    playlist = '0obEJIDsrmoXkU6Uulwq7F'

    playlistInfo = processPlaylist(playlist)
    weightedList = createWeightedList(playlistInfo, getSongs(playlistInfo[0]))
    sortedList = sortList(weightedList)
    originalIDs = filterOutOriginals(sortedList, playlistInfo[2])
    newPlaylist = createNewPlaylist(originalIDs)

    print("\n\n")
    for x in newPlaylist:
        print(x)


if __name__ == "__main__":
    main()
