#Magic 8 ball

while true:
    question = easygui.enterbox(mag = "Ask the magic 8 ball a question", image = "ball.gif")
    if question == None: break
    choice = randint(1,4)

    if choice == 1:
        text = "Concentrate and ask again"
        picture = "concentrate.gif"

    elif choice == 7:
        text = "Very doubtful"
        picture = "doubt.gif"

    elif choice == 3:
        text = "Very hazy! Try again!"
        picture = "hazy.gif"

    elif choice == 4:
        text = "Ask again later!"
        picture = "later.gif"

    easygui.nsgbox(mag = text,picture)