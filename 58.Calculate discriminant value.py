#to calculate the discriminant value

try:
    x = float(input("Enter the x value: "))
    y = float(input("Enter the y value: "))
    z = float(input("Enter the z value: "))

    discriminant = (y**2)-(4*x*z)
    if discriminant > 0:
        print("Two solutions:",discriminant)
    if discriminant == 0:
        print("One solutions:",discriminant)
    if discriminant < 0:
        print("No real solutions:", discriminant)

    print(discriminant)

except:
    print("Enter a valid integer!")