userInput = input('Please enter a line:')
alphaCounter = 0
numCounter = 0
for c in userInput:
    if c.isalpha():
        alphaCounter += 1
    if c.isdigit():
        numCounter += 1

print('Letter:' + str(alphaCounter))
print('Digit:' + str(numCounter))