#Count frequency of words in a dictionary

string = "apple banana cat dog cat elephant cat dog apple ant"
splitting = string.split()
frequency = [splitting.count(p) for p in splitting]
print(dict(zip(splitting,frequency)))