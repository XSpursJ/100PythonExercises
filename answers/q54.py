def flawed():

        a = 5 / 0


try:
    flawed()
except:
    print("division by zero!")
finally:
    print('In finally block for cleanup')
