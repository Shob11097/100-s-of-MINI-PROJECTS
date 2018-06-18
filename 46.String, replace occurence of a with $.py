#Replace all occurences of a in $ in a string:

try:
    string = input("Enter the string: ")
    s = string.replace('a','$')
    print(s)

except:
    print("Enter a valid string!")