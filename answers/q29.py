def printLongerString(s1, s2):
    if len(s1) > len(s2):
        print(s1)
    elif len(s1) < len(s2):
        print(s2)
    else:
        print(s1)
        print(s2)

printLongerString('fasd', 'fdsqe')
printLongerString('22222', 'fdsqe')
printLongerString('fasd312', 'fdsqe')
