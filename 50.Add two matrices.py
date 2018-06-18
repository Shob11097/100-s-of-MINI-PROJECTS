X = [[1,2,3],
     [5,3,6],
     [6,2,3]]

Y = [[4,7,3],
     [3,6,2],
     [1,6,7]]

result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

for i in range(len(X)):
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]
for r in result:
    print(r)