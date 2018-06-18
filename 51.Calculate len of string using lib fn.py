#Calculate length of the string using lib function

try:
    string = input("Enter the string: ")

    count = 0
    for i in string:
        count = count+1
    print(count)

except:
    print("Enter a valid string!")