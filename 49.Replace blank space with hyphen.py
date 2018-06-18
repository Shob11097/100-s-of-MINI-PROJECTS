#Replace with blank space with hyphen:

try:
    s1 = input("Enter the string: ")
    s2 = s1.replace(' ', '/')
    print(s2)

except:
    print("Enter a valid string!")