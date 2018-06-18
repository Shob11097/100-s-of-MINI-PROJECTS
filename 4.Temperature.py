#Test your program for several values for celsius and farenheit

try:
    x = input("Enter any temperature(Example: 12F/32C: ")
    if x[-1] == 'F':
        Celsius = int(x[:2])- 32
        C = Celsius * .55
        print(str(C) + "C")

    if x[-1] == 'C':
        Farenheit = int(x[:2])+ 32
        F = Farenheit * (9/5)
        answer = round(F)
        print(str(answer) + "F")

    else:
        print("It is an invalid input!")

except:
    print("The literal you typed is incorrect! Refer example!")



