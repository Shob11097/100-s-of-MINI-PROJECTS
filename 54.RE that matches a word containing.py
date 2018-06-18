#A word that matches containg s

import re
def match(text):
    pattern = 's\w*'
    if re.search(pattern, text):
        return "match found"
    else:
        return "match not found"
print(match("the snake is dead"))
print(match("The quick brown fox"))
