import re

pwList = input('Please enter passwords:').split(',')
printList = []

for pw in pwList:
    if len(pw) < 6 or len(pw) > 12:
        continue

    if not re.search('[a-z]', pw):
        continue
    elif not re.search('[A-Z]', pw):
        continue
    elif not re.search('[0-9]', pw):
        continue
    elif not re.search('[$#@]', pw):
        continue
    else:
        pass

    printList.append(pw)

print(printList)

    
