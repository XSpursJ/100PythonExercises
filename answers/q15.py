userInput = input('Enter a digit:')

if(len(userInput) != 1 or not userInput.isdigit()):
    print('Invalid input.')
    quit()

d = int(userInput)
result = d * 4 + d * 10 * 3 + d * 100 * 2 + d * 1000
print(result)
