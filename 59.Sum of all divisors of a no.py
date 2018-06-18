#To return sum of all divisors of a number:

try:
    l = []
    num = int(input("Enter the number: "))
    for i in range(1,num+1):
        if num%i ==0:
            l.append(i)
    print(l)

except:
    print("Enter a valid integer!")
