import random
li = [x for x in range(201) if x % 5 == 0 and x % 7 == 0]

for x in range(10):
    print(random.choice(li))
