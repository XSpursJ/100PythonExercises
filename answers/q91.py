class Person():
    def getGender(self):
        return 'unknown'

class Male(Person):
    def getGender(self):
        return 'Male'

class Female(Person):
    def getGender(self):
        return 'Female'

my1 = Person()
print(my1.getGender())
my2 = Male()
print(my2.getGender())
my3 = Female()
print(my3.getGender())
