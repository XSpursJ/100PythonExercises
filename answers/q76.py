import random

li = [x for x in range(100, 201) if x % 2 == 0]
print(random.sample(li, 5))
