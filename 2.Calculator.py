#CALCULATOR

try:
    number1 = int(input("what is the first number?"))
    operator = input("what do you want to do + - * /")
    number2 = int(input("what is the second number?"))

    if operator == "+":
        answer = number1 + number2
    elif operator == "-":
        answer = number1 - number2
    elif operator == "*":
        answer = number1 * number2
    elif operator == "/":
        answer = number1 / number2

    print("the answer is " + str(answer))

except:
    print("You have typed an invalid literal!")