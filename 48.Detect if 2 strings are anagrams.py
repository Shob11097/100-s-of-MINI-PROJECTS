#Detect if 2 strings are anagrams

try:
    s1 = input("Enter the string 1: ")

    s2 = input("Enter the string 2: ")

    if sorted(s1)==sorted(s2):
        print("The strings are anagrams!")
    else:
        print("The strings are not anagrams!")

except:
    print("Enter a valid string!")
