#To separate even and odd numbers in a separate list:

nums = range(1, 100)
list_even = [n for n in nums if n%2 == 0]
list_odd = [n for n in nums if n%2 == 1]
print("Odd numbers: "+ str(list_odd))
print("Even numbers: " +str(list_even))