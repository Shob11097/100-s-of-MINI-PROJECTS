#Sort the list of tuples in increasing order by the last element in each tuple

tuple1 = [(1,2),(3,4),(5,6),(7,8)]
h = sorted(tuple1, key=lambda x: x[-1])
print(h)
