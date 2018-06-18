#Binary equivalent of a number witout using recursion

try:
    n = int(input("Enter a number: "))
    binary = "{0:b}".format(n)
    print(binary)

except:
    print("Invalid literal for an integer!")