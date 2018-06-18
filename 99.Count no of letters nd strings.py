#Count no of letters and strings:

try:
    s = input("Input a string: ")
    d =l= 0
    for c in s:
        if c.isdigit():
            d=d+1
        elif c.isalpha():
            l=l+1
        else:
            pass

    print("Letters", l)
    print("Digits", d)

except:
    print("The input given here is incorrect!")