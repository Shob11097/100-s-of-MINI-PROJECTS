#Fizzbuzz game

counter = 0
while counter < 51:
    if counter % 5 == 0 and counter % 3 == 0:
        print("Fizzbuzz")
    elif counter % 3 == 0:
        print("Fizz")
    elif counter % 5 == 0:
        print("Buzz")
    else:
        print(counter)
    counter = counter+1