# Numbers in range which are perfect squares and sum of all digits in the number is less than 10

try:
    l = int(input("Enter lower range: "))
    u = int(input("Enter upper range: "))
    a = []
    a = [x for x in range(l,u+1) if (int(x**0.5))**2==x and sum(list(map(int,str(x))))<10]
    print(a)

except:
    print("Enter a valid input!")
