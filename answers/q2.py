tempNumber = -1
factorial = 1
try:
    tempNumber = int(input('Please enter a positive integer:'))
except:
    tempNumber = -1

if (tempNumber > 0):
    while(tempNumber > 0):
        factorial = factorial * tempNumber
        tempNumber -= 1
    print(factorial)
else:
    print('invalid input')
