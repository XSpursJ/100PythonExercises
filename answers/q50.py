class Circle(object):
    def __init__(self, r):
        self.radius = r

    def computeArea(self) -> float:
        return 3.1415926 * self.radius ** 2

mycircle = Circle(10)
print(mycircle.radius)
print(mycircle.computeArea())
