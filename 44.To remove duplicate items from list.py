#Remove duplicate items from list

try:
    c = []
    n = int(input("Enter the number of items: "))
    for i in range(1, n+1):
        d = int(input("Enter the items: "))
        c.append(d)
    print(c)

    a = list(set(c))
    print(a)

except:
    print("Enter a valid input!")
