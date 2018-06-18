#Multiplication table
try:
    n = int(input("Enter the number: "))
    for i in range(1,n+1):
        print(n,'x',i,'=',n*i)

except:
    print("Enter a valid integer!")