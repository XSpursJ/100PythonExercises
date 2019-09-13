try:
    n = int(input())
except:
    quit()

sum = 0
for x in range(n):
    sum += (x + 1)/(x + 2)
    print((x + 1)/(x + 2))

print(sum)
