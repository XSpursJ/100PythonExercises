def printTuple():
    l=[]
    t = ()
    for x in range(1, 21):
        l.append(x ** 2)

    t = tuple(l)
    print(t)
printTuple()
