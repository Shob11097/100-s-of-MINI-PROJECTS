#Python program to print an inverted star program:

max = 5
for x in range(1,max+1):
    for y in range(1,x+1):
        print("*",end='')
    print()

max = 4
for x in reversed(range(1,max+1)):
    for y in range(1,x+1):
        print("*",end='')
    print()