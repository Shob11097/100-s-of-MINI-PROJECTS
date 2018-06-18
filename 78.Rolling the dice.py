#Rolling the dice

import random

try:
    min = 1
    max = 6

    roll_again = "Yes"
    while roll_again == "Yes" or roll_again == "y":
        print("Rolling the dices...")
        print("The values are...")
        print(random.randint(min,max))
        print(random.randint(min, max))

        roll_again = input("Roll the dices again? (Yes/No )");

except:
    print("The input given is wrong!")