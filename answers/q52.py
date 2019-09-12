class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, l):
        self.length = l

    def area(self):
        return self.length ** 2

myshape = Shape()
print(myshape.area())

mysquare = Square(3)
print(mysquare.length)
print(mysquare.area())
