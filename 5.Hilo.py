#Hilo game

from random import randint
x = randint(1,50)

try:
    Name = input("May i know your name?: ")
    print("Hey " + Name + "! Choose any number between 1 to 50! You have 5 chances!")
    guess = 0
    tries = 0

    while guess < 10:
        tries = tries + 1
        guess = int(input("What is your guess?"))
        if guess < x:
            print("Your guess is too low!")
        if guess > x:
            print("Your guess is too high!")
        if guess == x:
           print("you won")
    if guess == x:
        print("you won")

except:
    print("It is an invalid input!")


