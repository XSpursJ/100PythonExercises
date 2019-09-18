s = input()
s1 = [s[x] for x in range(len(s)) if x % 2 == 0]
print(''.join(s1))

# s=input()
# s = s[::2]
# print(s)
