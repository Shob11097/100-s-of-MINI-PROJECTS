#Gravitational force

try:
    m1 = float(input("Enter the first mass: "))
    m2 = float(input("Enter the second mass: "))
    r = float(input("Enter the distance between the centres of the masses: "))
    G = 6.673*(10**-11)
    Formula = (G*m1*m2)/(r**2)
    print("Hence, the gravitational force is: ",float(Formula,2) + "N")

except:
    print("The input given is wrong!")