#List of tuples as 1st element as number and 2nd element as squares

number = range(1, 20)
a = [(x,x*x) for x in number]
print(a)