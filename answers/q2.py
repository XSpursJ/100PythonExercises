tempNumber = -1
factorial = 1
try:
    tempNumber = int(raw_input('Please enter a non-negative integer:'))
except:
    tempNumber = -1

if (tempNumber == 0):
    factorial = 1
    print(factorial)
elif(tempNumber > 0):
    while(tempNumber > 0):
        factorial = factorial * tempNumber
        tempNumber -= 1
    print(factorial)
else:
    print('invalid input')
