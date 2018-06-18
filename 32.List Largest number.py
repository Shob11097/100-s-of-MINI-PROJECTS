#Find the largest number in a list!

try:
    a = []
    n = int(input("Enter the number of elements: "))
    for i in range(1, n+1):
        b = int(input("Enter the element: "))
        a.append(b)
    a.sort()
    print("Largest element: ",a[-1])

except:
    print("Enter a valid input!")