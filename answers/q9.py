lines = []

while True:
    s = input('Enter your line:')
    if s:
        lines += [s.upper()]
    else:
        break


for line in lines:
    print(line)