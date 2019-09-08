userInput = input("Please enter the list:").split(',')

list = [x for x in userInput if int(x) % 2 != 0]
print(list)
