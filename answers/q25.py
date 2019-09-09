class myClass:
    p = 123

    def __init__(self, n):
        self.p = n


x = myClass(999)
print(x.p)
print(myClass.p)
