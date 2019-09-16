li = [12,24,35,70,88,120,155]

li2 = [x for (i, x) in enumerate(li) if i not in [0, 4, 5]
print(li2)
