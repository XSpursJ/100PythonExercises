def myGenerator(n):
    for x in range(n + 1):
        if x % 5 == 0 and x % 7 == 0:
            yield x

try:
    n = int(input())
except:
    print('Please enter positive integer only!')
    n = 0

if n >= 0:
    l = [x for x in myGenerator(n)]
    print(l)
