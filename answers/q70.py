li = [x for x in range(101)]

def searchValue(x, l):
    start = 0
    stop = len(l)
    mid = int(round((start + stop) / 2))
    while start < stop:
        if l[mid] == x:
            return mid
        elif l[mid] < x:
            start = mid
            if mid != int(round((start + stop) / 2)):
                mid = int(round((start + stop) / 2))
            else:
                break
        else:
            stop = mid
            if mid != int(round((start + stop) / 2)):
                mid = int(round((start + stop) / 2))
            else:
                break
        print(start, mid, stop)
    return -1

print(searchValue(100, li))
print(searchValue(12, li))
