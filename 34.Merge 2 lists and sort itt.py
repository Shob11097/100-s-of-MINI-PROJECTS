#Merge 2 lists and sort it

try:
    list_1 = []
    list_2 = []
    n1 = int(input("Enter the number elements for list1: "))
    n2 = int(input("Enter the number elements for list2: "))

    for n in range(1, n1+1):
        a = int(input("Enter the elements: "))
        list_1.append(a)
    for n in range(1, n2+1):
        b = int(input("Enter the elements: "))
        list_2.append(b)
    append = list_1+list_2
    append.sort()
    print(append)

except:
    print("The number should be in integer!")
