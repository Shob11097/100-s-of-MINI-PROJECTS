#Prime factors

try:
    x = int(input("Enter the number: "))
    for i in range(1,x+1):
        if x%i == 0:
            print(i)

except:
    print("Only integers are allowed!")