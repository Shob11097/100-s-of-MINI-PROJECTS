#Leap year!

try:
    year = int(input("Enter the year you wanted to check! "))

    if (year%4) == 0:
        if (year%100) == 0:
            if (year%400) == 0:
                print("Its a leap year! ")
    else:
        print("Its not a leap year")

except:
    print("The value entered is invalid!")