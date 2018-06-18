# Second largest number in a list:

try:
    number = []
    n = int(input("Enter the number of items: "))

    for n in range(1, n+1):
        a = int(input("Enter the elements: "))
        number.append(a)
    number.sort()
    print("The second largest element: ", number[-2])

except:
    print("The value entered has been wrong!")