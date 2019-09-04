s = input("Enter a comma seperated string:")
l = []

if(len(s) <= 0):
    print('Empty input!')
else:
    startCommaIndex = 0
    stopCommaIndex = 0
    appearance = s.count(',')

    for x in range(appearance + 1):
        stopCommaIndex = s.find(',', startCommaIndex)
        if(stopCommaIndex != -1):
            temp = s[startCommaIndex : stopCommaIndex].strip()
            startCommaIndex = stopCommaIndex + 1
        else:
            temp = s[startCommaIndex : len(s)].strip()

        if(temp != ''):
            l += [temp]
    t = tuple(l)
    print(l)
    print(t)

# Solution:
# values=raw_input()
# l=values.split(",")
# t=tuple(l)
# print l
# print t.




#testing merging 2 different branches
