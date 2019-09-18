li1 = [12,24,35,24,88,120,155,88,120,155, 5]
set1 = set(li1)

li2 = []
for x in li1:
    if x in set1:
        li2.append(x)
        set1.remove(x)
print(li2)
