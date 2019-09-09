oldList = sorted(input('Enter a paragraph:').split())
print(oldList)
printList = []
i = 0
length = len(oldList)
occurance = 1
while i < length:
    j = i + 1
    if j < length:
        while oldList[i] == oldList[j]:
            occurance += 1
            j += 1
            if j == length:
                break

    printList.append(oldList[i] + ':' + str(occurance))
    i = j
    occurance = 1

    

    if i >= length:
        break

for item in printList:
    print(item)
