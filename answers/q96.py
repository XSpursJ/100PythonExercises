def solve(h, l):
    for x in range(1, h+1):
        y = h - x
        if x * 2 + y * 4 == l:
            return x,y
    return 'No Solution'

head = 35
leg = 94

print(solve(head,leg))
