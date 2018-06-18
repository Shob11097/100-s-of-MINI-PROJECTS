#LCM

try:
    a = int(input("Enter the number 1: "))
    b = int(input("Enter the number 2: "))

    def gcd(a,b):
        while b > 0:
            a, b = b,a % b
        return a

    def lcm(a,b):
        return a * b / gcd(a,b)

    print(lcm(a,b))

except:
    print("It is an invalid input!")