m = [[1, 2, 3],  [4, 5, 6],  [7, 8, 9]]
n = [[2, 2, 2],  [3, 3, 3],  [4, 4, 4]]
print( list(zip(m, n)))
print( *zip(m, n))
print(list(zip(zip(m,n))))
print(list(zip(*zip(m,n))))
print(*zip(zip(m,n)))



