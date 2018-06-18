#To convert the height from centimeters to feet and inches:

try:
    Centimeter = int(input("Enter your heights in cm =  "))

    Feet = 0.0328*Centimeter

    Inches = 0.0328*Centimeter

    print("The height in inches = "+ str(Inches))

    print("The height in Feet = "+ str(Feet))

except:
    print("The entered is invalid!")