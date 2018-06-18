#Fibonacci sequence


n = 10
num_1 = 0
num_2 = 1
count = 0

if n <= 0:
        print("Enter a positive integer!")
elif n == 0:
        print(num_1)
else:
        print("Fibonacci sequence upto n: ")
        while count < n:
            print(num_1,end =',')
            nth = num_1 +num_2
            num_1 = num_2
            num_2 = nth
            count += 1