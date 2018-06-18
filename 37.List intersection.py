#Interesection of list

try:
    def intersection(a,b):
        return list(set(a) & set(b))

    def intersect():
        list_1 = []
        list_2 = []

        n1 = int(input("Enter the number elements for list1: "))
        n2 = int(input("Enter the number elements for list2: "))

        for n in range(1, n1+1):
            a = int(input("Enter the elements for list1: "))
            list_1.append(a)
        for n in range(1, n2+1):
            b = int(input("Enter the elements for list2: "))
            list_2.append(b)
        print(intersection(list_1, list_2))
    intersect()

except:
    print("Enter a valid input!")