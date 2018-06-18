# Hangman game

Name = input("May i know your name: ")
print("Lets start the hangman game!")
print("Guess the character(Lower case letters should be used!!")

word = "python"
guesses = " "

turns = 10
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("-")
            failed += 1
    if failed == 0:
        print("You won!")
        break

    guess = input("Guess the character : ")
    guesses += guess
    if guess not in word:
        turns -= 1
    print("Wrong! You have " + str(turns) + " more guesses!")



