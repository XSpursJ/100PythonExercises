import random
li = [x for x in range(11) if x % 2 == 0]

for x in range(10):
    print(random.choice(li))
