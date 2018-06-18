#Reg ex group extraction

import re
str = "hello wprld shobana.amir@gmail.com apple banana cat dog"
match = re.search('([\w.]+)@([\w.-]+)',str)
if match:
    print(match.group())
    print(match.group(1))
    print(match.group(2))