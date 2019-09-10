t1 = (1,2,3,4,5,6,7,8,9,10)
l1 = list(t1)
l2 = [l1[x] for x in range(len(t1)) if l1[x] % 2 == 0]
t2 = tuple(l2)
print(t2)
