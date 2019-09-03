#
tempString = ''
for x in range(2000, 3200):
    if(x % 7 == 0):
        if(x % 5 != 0):
            if(tempString == ''):
                tempString += str(x)
            else:
                tempString += (',' +str(x))
#print final result
print(tempString)

# solution:
# l=[]
# for i in range(2000, 3201):
#     if (i%7==0) and (i%5!=0):
#         l.append(str(i))
#
# print ','.join(l)
