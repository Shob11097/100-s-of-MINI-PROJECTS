#Remove the nth index character from a non-empty string:

def remove(string, n):
    first = string[:n]
    middle = string[n+1:]
    return first+middle
string = input("Enter the string: ")
n = int(input("Enter the index of the character to remove: "))
print(remove(string, n))

