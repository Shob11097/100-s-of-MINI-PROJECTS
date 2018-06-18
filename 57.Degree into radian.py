#Convert degree into radian

try:
    pi = 22/7
    degree = float(input("Enter the degree: "))
    radian = degree*(pi/180)
    print(radian)

except:
    print("A invalid character has been entered!")