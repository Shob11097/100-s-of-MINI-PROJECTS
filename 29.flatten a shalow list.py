import itertools
l = [[4,5,3],[5,6,2], [4],[6,5],  [2,5,9]]
a = list(itertools.chain(*l))
print(a)