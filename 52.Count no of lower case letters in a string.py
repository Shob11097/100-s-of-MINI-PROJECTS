#Count no of lower case letters in a string:

string = "Apple A Day Keeps A Doctor Away"
count = 0
for i in string:
    if (i.islower()):
        count = count+1
print(count)
