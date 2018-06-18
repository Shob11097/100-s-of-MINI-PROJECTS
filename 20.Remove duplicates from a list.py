#program to remove duplicates from a list of lists.

num = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
hey = set(map(tuple,num))
b = map(list,hey)
print(hey)
