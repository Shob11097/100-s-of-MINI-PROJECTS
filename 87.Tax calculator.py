#Tax calculator

try:
    Amount = int(input("Enter the amount you wanted to calculate!"))
    taxRate = 0.13
    tax = Amount*taxRate
    totalPrice = Amount + tax
    print("The total amount will be " + str(totalPrice) )

except:
    print("The input given here is incorrect!")