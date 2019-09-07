printList = []
for x in range(1000, 3001):
    count = 0
    for c in str(x):
        if int(c) % 2 == 0:
            count += 1
    if(count >= 4):
        printList += [str(x)]
print(','.join(printList))