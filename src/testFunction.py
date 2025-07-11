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




lst = []




average = getAverage(lst)


low = findCutOff(lst, round(average * 0.01))
mid = findCutOff(lst, round(average * 0.25))
high = findCutOff(lst, round(average * 0.5))


print(lst[0:high])
print("\n\n")
print(lst[high:mid])
print("\n\n")
print(lst[mid:low])