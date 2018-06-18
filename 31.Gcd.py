#GCD

try:
    a = int(input("Enter the number 1: "))
    b = int(input("Enter the number 2: "))

    def gcd(a,b):
        while b > 0:
            a, b = b,a % b
        return a
    print(gcd(a,b))

except:
    print("Enter a valid input!")