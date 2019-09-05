class Teststrings:
    stop = 0
    def __init__(self, s):
        self.inputString = s
        self.outputString = s

    def getStringFromConsole(self, s):
        self.inputString = input(s)
        if(self.inputString == 'done'):
            self.stop = 1

    def printString(self):
        self.outputString = self.inputString.upper()
        print(self.inputString)
        print(self.outputString)


def testFunction():
    teststrings = Teststrings('from test function')
    print('input string is:' + teststrings.inputString)
    print('output string is:' + teststrings.outputString)
    while(teststrings.stop == 0):
        teststrings.getStringFromConsole('provide a lower case string:')
        teststrings.printString()

testFunction()
