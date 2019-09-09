l = []
while True:
    s = input('Enter a tuple:')
    if s:
        l.append(tuple(s.split(',')))
    else:
        break

print(sorted(l))
