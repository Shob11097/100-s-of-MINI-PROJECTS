#Generate a dict in form (2,4)

try:
    num = int(input("Enter the number! "))
    for i in range(1,num):
        dict = {i:i*i}
        print(dict)

except:
    print("Enter the valid integer!")