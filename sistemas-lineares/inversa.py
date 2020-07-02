from solution import *

def inversa(a, n):
  mat = [[0 for _ in range(n)] for __ in range(n)]
  for i in range(n):
    x = [1 if j == i else 0 for j in range(n)]
    sol = solveLU(a, x, n)
    for j in range(n):
      mat[j][i] = sol[j]
  return mat


mat = [[1,1,0,2], [1,2,-2,0], [0,-2,5,1], [2,0,1,18]]

print(*inversa(mat, 4))
