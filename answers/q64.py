def fibonacci(n : int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

try:
    n = int(input())
except:
    print('Something wrong')
    quit()

if(n < 0):
    print('Invalid input')
else:
    print(fibonacci(n))
