#To check if a triangle is equilateral,isoceles, or scalene!

try:
    print("Lengths of the triangle! ")
    x = int(input("Enter the x value: "))
    y = int(input("Enter the y value: "))
    z = int(input("Enter the z value: "))

    if x == y == z:
        print("Its an Equilateral triangle!")
    elif x != y != z:
        print("Its an Scalene triangle")
    else:
        print("Its an Isosceles triangle!")

except:
    print("Enter a valid integer!")
