#Program to find sequences of lowercase letters joined with a underscore

import re
def match(text):
    pattern = '^[a-z]+_[a-z]'
    if re.search(pattern,text):
        return 'found a match'
    else:
        return "not matched"
print(match("aaaaa_hashddfh"))