#Generate random numbers from 1 to 20 and append them in a list

try:
        import random
        a = []
        n = int(input("Enter the numbers: "))
        for i in range(n):
                a.append(random.randint(1, 20))
        print(a)

except:
    print("Enter a valid input!")