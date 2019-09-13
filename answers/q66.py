def myGenerator(n : int):
    for x in range(n + 1):
        if x % 2 == 0:
            yield x

l = [x for x in myGenerator(10)]
print(l)
