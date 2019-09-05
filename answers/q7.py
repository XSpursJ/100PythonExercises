userInput = input('Please enter the number of rows and columns:').split(',')
try:
    row = int(userInput[0])
    column = int(userInput[1])
except:
    print('invalid input.')

rowList = []


if(row > 0 and column > 0):
    for i in range(row):
        columnList = []
        for j in range(column):
            columnList += [(i * j)]
        rowList += [columnList]
    print(rowList)
