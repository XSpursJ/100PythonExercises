userInput = input('Please enter a line:')
uc = 0
lc = 0

for c in userInput:
    if c.isupper():
        uc += 1
    if c.islower():
        lc += 1
print('Upper case:' + str(uc))
print('Lower case:' + str(lc))
