l1 = [1,2,3,4,5,6,7,8,9,10]

l2 = [x for x in filter(lambda i: i % 2 == 0, l1)]

l3 = [x for x in map(lambda i: i ** 2, l2)]

print(l3)
