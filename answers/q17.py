balance = 0
while True:
    s = input('Please enter a transaction:')
    if s:
        t = s.split()
        if t[0] == 'D':
            balance += int(t[1])
        elif t[0] == 'W':
            balance -= int(t[1])
        else:
            print("Invalid input.")
    else:
        break

print('Balance:' + str(balance))
