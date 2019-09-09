def printL():
    l = []
    for x in range(1, 21):
        l.append(x**2)

    for x in range(len(l) - 5, len(l)):
        print(l[x])

printL()
