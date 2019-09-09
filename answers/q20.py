class iterate7:
    def __init__(self):
        self.start = 0

    def generator(self, n):
        x = self.start
        while x < n:
            if x % 7 == 0:
                yield x
            x += 1
        

l = iterate7()

for x in l.generator(100):
    print(x)
