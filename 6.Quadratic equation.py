#Quadratic equation to calculate  the discriminant:

try:
    import cmath
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    c = int(input("Enter the value of c: "))

    Quadratic_equation = (b**2)-(4*a*c)/(2*a)
    print("The discriminant values are: " + str(Quadratic_equation))

    Solution_1 = (-b-cmath.sqrt(Quadratic_equation))
    Solution_2 = (-b+cmath.sqrt(Quadratic_equation))
    print("Solution 1 is = " + str(Solution_1))
    print("Solution 2 is = " +str(Solution_2))

except:
    print("Enter the valid input!")