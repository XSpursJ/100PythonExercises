userInput = input("Please enter 4-digit binary numbers:").split(',')
numberList = []
printList = []
for item in userInput:
    try:
        if int(item, 2) % 5 == 0:
            printList += [item]
    except:
        pass

print(printList)