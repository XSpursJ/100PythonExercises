import math

def calculateQ(d):
    return (round(math.sqrt((2 * 50 * d) / 30)))

inputList = []
outputList = []

inputList = input('please input numbers separated by comma').split(',')
for x in inputList:
    outputList += [calculateQ(float(x))]

print(inputList)
print(outputList)
