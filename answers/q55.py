class MyException(Exception):
    def __init__(self, s : str):
        self.message = s

try:
    raise MyException('Hello')
except MyException as aa:
    print(aa.message)
