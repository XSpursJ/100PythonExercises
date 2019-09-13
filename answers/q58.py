import re
words = input().split()

for word in words:
    if re.match('\d+', word) != None:
        print(word)
