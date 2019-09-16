from timeit import Timer


t = Timer('1 + 1')
print(t.timeit(100))
