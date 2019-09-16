import random
li = [x for x in range(1, 1001) if x % 5 == 0 and x % 7 == 0]

print(random.sample(li, 5))
