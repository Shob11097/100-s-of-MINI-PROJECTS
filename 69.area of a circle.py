#To find the area of a circle!

try:
    from math import pi
    r = float(input("Enter the radius of the circle: "))
    print("The area of the circle: "+str(pi*(r**2)))
    print("The circumference of the circle: "+str(2*pi*r))

except:
    print("Enter a valid integer!")