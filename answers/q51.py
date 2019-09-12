class Rectangle:
    def __init__(self, x:float, y:float):
        '''initialize the length and width'''
        self.length = x
        self.width = y

    def computeArea(self) -> float:
        return self.length * self.width

myrec = Rectangle(10, 20)
print(myrec.computeArea())
print(myrec.length)
