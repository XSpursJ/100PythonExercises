def rec(n):
    if n > 0:
        return 100 + rec(n - 1)
    elif n == 0:
        return 1
    else:
        return 0

try:
    n = int(input())
except:
    print('something wrong')

if(n < 0):
    print('invalid input!')
else:
    print(rec(n))
