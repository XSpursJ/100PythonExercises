import re
email = 'john@google.com'
pattern = '(\w+)@(\w+)+(\.com)'
reobject = re.match(pattern, email)



print(reobject.group(2))
