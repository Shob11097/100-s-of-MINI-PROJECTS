from math import sqrt

try:
    print("Pythagorean theorem calculator!")
    print('Assume that the sides are a,b,c where c is the hypotenuse(The side opposite to the right angle!')
    side = input("Which side do you want to calculate? (a, b, c) : ")

    if side == "a":
        b_value = int(input("Enter the length of the side b: "))
        c_value = int(input("Enter the length of the side c: "))

        a_value = sqrt((c_value * c_value)-(b_value * b_value))
        print("The length of the side a is: ", a_value)
    elif side == "b":
        a_value = int(input("Enter the length of the side a: "))
        c_value = int(input("Enter the length of the side c: "))

        b_value = sqrt((c_value * c_value)-(b_value * b_value))
        print("The length of the side b is: ", b_value)

    elif side == "c":
        a_value = int(input("Enter the length of the side a: "))
        b_value = int(input("Enter the length of the side b: "))

        c_value = sqrt((a_value * a_value)+(b_value * b_value))
        print("The length of the side c is: ",c_value )

    else:
        print("Select a side between a,b,c")

except:
    print("Enter a valid integer")