tempNumber = 0
try:
    tempNumber = int(input('Pelase type a positive integer:'))
except:
    print("Invalid input.")

d = dict()

if(tempNumber > 0):
    for i in range(1, tempNumber + 1):
        d[i] = i * i
    print(d)
else:
    print("You need to enter a positive integer.")
