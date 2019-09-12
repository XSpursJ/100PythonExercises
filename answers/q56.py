email = 'john@google.com'

indexOfAt = email.find('@')
indexOfDot = email.find('.')
userName = email[:indexOfAt]
companyName = email[indexOfAt + 1 : indexOfDot]

print(userName)
print(companyName)

# answer:
# import re
# emailAddress = input()
# pat2 = "(\w+)@((\w+\.)+(com))"
# r2 = re.match(pat2,emailAddress)
# print (r2.group(1))
