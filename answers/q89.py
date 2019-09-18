# li1 = [1,3,6,78,35,55, 24]
# li2 = [12,24,35,24,88,120,155]
#
# li3 = [x for x in li1 if x in li2]
# print(li3)


# answer:
set1=set([1,3,6,78,35,55,24,24])
set2=set([12,24,35,24,88,120,155])
set1 &= set2
li=list(set1)
print(li)
