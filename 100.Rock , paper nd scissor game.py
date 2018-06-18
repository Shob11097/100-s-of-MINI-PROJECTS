import random

moves = ['rock','paper','scissor']
play = "true"

while play == "true":
    cmove = random.choice(moves)
    pmove = input("What is your move? (rock/paper/scissor) ")
    print("The computer chose", cmove)

    if cmove == pmove:
        print("Tie")
    elif pmove == "rock" and cmove == "scissor":
        print("Player wins!")
    elif pmove == "rock" and cmove == "paper":
        print("Computer wins!")
    elif pmove == "paper" and cmove == "scissor":
        print("Computer wins!")
    elif pmove == "paper" and cmove == "rock":
        print("Player wins!")
    elif pmove == "scissor" and cmove == "rock":
        print("Computer wins!")
    elif pmove == "scissor" and cmove == "paper":
        print("Player wins!")