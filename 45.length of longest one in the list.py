#Read a list of words and return the length of the longest one

print(max(['a','cat','sat','goat'],
key = lambda s: (len(s), s)))

