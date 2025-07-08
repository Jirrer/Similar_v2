from ProcessUserPlaylist import processPlaylist, getOriginalSongs
import random

newPlaylistLength = 30 # number of new songs
similarityLowLevel = 3.0 # minimum level of similarity 

def getSongs():
    





    temp = [
        ['4F84IBURUo98r4r61KF70', 'rap rock', '1E4r4z7ivGUcSAnCbINJ9v'],
        ['7oPftvlw6VrsViSDV7fJY', 'pop punk,thrash metal', '6eUKZXaKkcviH0Ku9w2n3V'],
        ['0yN7xI1blow9nYIKR8nM7', 'christian,pop punk,hard rock', '2ye2Wgw4gimLv2eAKyk1NB'],
        ['0yN7xI1blw9nYIK0R8nM7', 'funk rock,horror punk,industrial metal', '2ye2Wgw4gimLv2eAKyk1NB'],
        ['7jyrLJdDQY21OgRLCZ9sD', 'industrial metal,rap metal,heavy metal', '2xiIXseIJcq3nG7C8fHeBj'],
        ['6olE6TJLqE3rqDCT0FyPh', 'emo,punk,alternative rock', '3TOqt5oJwL9BE2NG9MEwDa'],
        ['6olE6TJLqED3rqCT0FyPh', 'emo', '3TOqt5oJwL9BE2NG9MEwDa'],
        ['0yN7x1blow9nYIK0R8nM7', 'funk rock', '2ye2Wgw4gimLv2eAKyk1NB'],
        ['6deZN1blXzeGvOLaLMOIF', 'pop punk', '711MCceyCBcFnzjGY4Q7Un'],
        ['6deZN1bslXzGvOLaLMOIF', 'hardcore punk', '711MCceyCBcFnzjGY4Q7Un'],
        ['5CtI0qwDJkDQwXD1H1cLb', 'punk,horror punk', '1Xyo4u8uXC1ZmMpatF05PJ'],
        ['5LfGQac0EIXyAN8UwmNAQ', 'modern blues,post-grunge,art rock', '6gZq1Q6bdOxsUPUG1TaFbF'],
        ['6deZN1bslXzeGvOLLMOIF', 'garage rock,country rock', '711MCceyCBcFnzjGY4Q7Un'],
        ['5CtI0qwDJkDQGwXDH1cLb', 'country,metal', '1Xyo4u8uXC1ZmMpatF05PJ'],
        ['3n3Ppam7vgaV1iaRUc9Lp', 'groove metal', '3YcBF2ttyueytpXtEzn1Za'],
        ['0yN7x1blownYIK0R8nM7', 'groove metal,christian alternative rock', '2ye2Wgw4gimLv2eAKyk1NB'],
        ['64tNs6TnZe2zpcMVMOoHL', 'country rock', '165ZgPlLkK7bf5bDoFc6Sb'],
        ['43swHjahvgbx1WNIkIz', 'punk,art rock', '5eAWCfyUhZtHHtBdNk56l1'],
        ['64sm6TnZe2zpcMVMOoHL', 'grunge,country', '165ZgPlLkK7bf5bDoFc6Sb'],
        ['6deZbslXzeGvOLaLMOIF', 'christian alternative rock', '711MCceyCBcFnzjGY4Q7Un'],
        ['3n3Ppam7aVa1iaRUc9Lp', 'rock,horror punk,rap metal', '3YcBF2ttyueytpXtEzn1Za'],
        ['7jy3rLJdD21OgRLCZ9sD', 'rock', '2xiIXseIJcq3nG7C8fHeBj'],
        ['0yN7xI1blo9nYIK0R8nM7', 'christian alternative rock,thrash metal', '2ye2Wgw4gimLv2eAKyk1NB'],
        ['3n3Ppm7vaVa1iaRUc9Lp', 'funk rock,christian rock,rock', '3YcBF2ttyueytpXtEzn1Za'],
        ['5LfGQaEIXyAN8aUwmNAQ', 'horror punk,country', '6gZq1Q6bdOxsUPUG1TaFbF'],
        ['3n3PpamgaVa1RUc9Lp', 'country hip hop', '3YcBF2ttyueytpXtEzn1Za'],
        ['7jy3rLJdDQY2gRLCZ9sD', 'art rock,garage rock', '2xiIXseIJcq3nG7C8fHeBj'],
        ['7jy3rLJdDQY2gRLCZ9sD', 'blues rock,horror punk', '2xiIXseIJcq3nG7C8fHeBj'],
        ['43sZBwHjaUvx1WNIkIz', 'heavy metal,horror punk', '5eAWCfyUhZtHHtBdNk56l1'],
        ['3n3Ppam7vaVa1iaRUc9Lp', 'grunge,nu metal,rap rock', '3YcBF2ttyueytpXtEzn1Za'],
        ['6olE6TJLqED3qDCT0FyPh', 'heavy metal,modern blues', '3TOqt5oJwL9BE2NG9MEwDa'],
        ['3n3Ppam7vga1iaRUc9Lp', 'christian alternative rock', '3YcBF2ttyueytpXtEzn1Za'],
        ['7jy3rLJdDQY21gRLCZ9sD', 'art rock,southern hip hop', '2xiIXseIJcq3nG7C8fHeBj'],
        ['6deZN1bslXzOLaLMOIF', 'metal,hardcore punk,emo', '711MCceyCBcFnzjGY4Q7Un'],
        ['4F84IBURUo984r61KF70', 'pop punk', '1E4r4z7ivGUcSAnCbINJ9v'],
        ['7jy3rLJdDQY21OgRZ9sD', 'rap metal', '2xiIXseIJcq3nG7C8fHeBj'],
        ['64tNsm6TnZe2zMVMOoHL', 'metalcore,horror punk,alternative rock', '165ZgPlLkK7bf5bDoFc6Sb'],
        ['4F84IBURUo98rz4rKF70', 'screamo,industrial metal,christian alternative rock', '1E4r4z7ivGUcSAnCbINJ9v'],
        ['4F84IBURUo9z4r61KF70', 'christian alternative rock,metal,rock', '1E4r4z7ivGUcSAnCbINJ9v'],
        ['n3Ppam7vga1iaRUc9Lp', 'christian rock,post-grunge', '3YcBF2ttyueytpXtEzn1Za'],
        ['7oPftvlwr6VrsViSDV7fJY', 'country', '6eUKZXaKkcviH0Ku9w2n3V'],
        ['64tNsm6TnZe2cMVMOoHL', 'post-hardcore,groove metal,blues rock', '165ZgPlLkK7bf5bDoFc6Sb'],
        ['5t28BP2x2axFnqOOMg3CM', 'hard rock,garage rock,funk rock', '6XyY86QOPPrYVGvF9ch6wz'],
        ['6olE6JLqED3rqDCT0FyPh', 'rap metal,grunge', '3TOqt5oJwL9BE2NG9MEwDa'],
        ['6olE6TJLqD3rqDCT0FyPh', 'country,rap rock,country hip hop', '3TOqt5oJwL9BE2NG9MEwDa'],
        ['6olE6TJLqED3rqDCT0FyPh', 'rap rock', '3TOqt5oJwL9BE2NG9MEwDa'],
        ['43sZBwHjahvgbx1WNIkIz', 'screamo', '5eAWCfyUhZtHHtBdNk56l1'],
        ['64tNsm6TnZe2zpcMVMOoHL', 'garage rock', '165ZgPlLkK7bf5bDoFc6Sb'],
        ['6deZN1bsleGvOLaLMOIF', 'modern blues,hard rock', '711MCceyCBcFnzjGY4Q7Un'],
        ['6deZN1bslXzeGvOLaLMOIF', 'rock', '711MCceyCBcFnzjGY4Q7Un'],
        ['5t28BP42xaxFnqOOMg3CM', 'nu metal', '6XyY86QOPPrYVGvF9ch6wz'],
        ['64tNsm6Ze2zpcMVMOoHL', 'thrash metal,christian,metalcore', '165ZgPlLkK7bf5bDoFc6Sb'],
        ['5t28BP42x2axFnqOOMg3CM', 'industrial metal,horror punk,alternative metal', '6XyY86QOPPrYVGvF9ch6wz'],
        ['6deZN1bXzeGvOLaLMOIF', 'grunge,alternative rock', '711MCceyCBcFnzjGY4Q7Un'],
        ['3n3Ppam7vgaVa1iaRUc9Lp', 'southern hip hop', '3YcBF2ttyueytpXtEzn1Za'],
        ['7ftvlwr6VrsViSDV7fJY', 'rock,country hip hop,pop punk', '6eUKZXaKkcviH0Ku9w2n3V'],
        ['6deZ1bseGvOLaLMOIF', 'skate punk', '711MCceyCBcFnzjGY4Q7Un'],
        ['5CtwDJkDQGwXDH1cLb', 'rock', '1Xyo4u8uXC1ZmMpatF05PJ'],
        ['7oPftvlwr6VrsSDV7fJY', 'christian', '6eUKZXaKkcviH0Ku9w2n3V'],
        ['0yN7xI1blow9nY0R8nM7', 'modern blues,christian rock', '2ye2Wgw4gimLv2eAKyk1NB'],
        ['7jy3rLJdDQY21OgRLCZ9sD', 'country hip hop', '2xiIXseIJcq3nG7C8fHeBj'],
        ['3n3Ppam7vga1iaUc9Lp', 'pop punk,rap metal', '3YcBF2ttyueytpXtEzn1Za'],
        ['5CtI0qwDJkGwXD1H1cLb', 'metalcore,garage rock,rap metal', '1Xyo4u8uXC1ZmMpatF05PJ'],
        ['3n3Ppam7vgaVa1iUc9Lp', 'country rock,horror punk,thrash metal', '3YcBF2ttyueytpXtEzn1Za'],
        ['3rjM7GhxdVq1YySsHBS21i', 'punk,skate punk', '3TOqt5oJwL9BE2NG9MEwDa']
    ]

    return temp

def createWeightedList(playlistInfo):
    songsFromDB = getSongs()

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

def createNewPlaylist(lst):
    global newPlaylistLength

    seen = set()
    unique_lst = []
    for item in lst:
        if item[0] not in seen:
            unique_lst.append(item)
            seen.add(item[0])

    total = len(unique_lst)
    if total < newPlaylistLength:
        raise ValueError("Not enough unique songs to fill the playlist.")

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
    
def filterOutOriginals(candidateList, originalIDs):
    return [item for item in candidateList if item[0] not in originalIDs]

def main():
    playlistInfo = processPlaylist('0obEJIDsrmoXkU6Uulwq7F')
    weightedList = createWeightedList(playlistInfo)
    sortedList = sortList(weightedList)
    originalSongs = filterOutOriginals(sortedList, getOriginalSongs('0obEJIDsrmoXkU6Uulwq7F'))
    newPlaylist = createNewPlaylist(originalSongs)



    print(len(newPlaylist))
    for x in newPlaylist:
        print(x)


if __name__ == "__main__":
    main()
