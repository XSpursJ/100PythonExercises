import math

x = 0
y = 0

while True:
    try:
        s = input('Enter a command:')
        if s:
            l = s.split()
            cmd = l[0]
            step = int(l[1])
            if cmd == 'UP':
                y += step
                print('y:' + str(y))
            elif cmd == 'DOWN':
                y -= step
                print('y:' + str(y))
            elif cmd == 'LEFT':
                x -= step
                print('x:' + str(x))
            elif cmd == 'RIGHT':
                x += step
                print('x:' + str(x))
            else:
                print('Invaled Input:')
        else:
            break
    except:
        print('ERROR:')

d = int(round(math.sqrt( x * x + y * y)))
print(d)
