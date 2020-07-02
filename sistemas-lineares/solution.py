from matrix import *
from math import sqrt

def fatLU(mat, n):
  l = id(n)
  u = [[mat[i][j] for j in range(n)] for i in range(n)]
  swaps = []
  for j in range(0, n):
    if u[j][j] == 0:
      for i in range(j+1, n):
        if u[i][j]:
          u[j], u[i] = u[i], u[j]
          swaps.append((i, j))
          break
    m = id(n)
    for i in range(j+1, n):
      l[i][j] = u[i][j] / u[j][j]
      m[i][j] = -l[i][j]
    u = prod(m, u, n)
  return l, u, swaps


def triangularSuperior(a, b, n):
  x = [0 for _ in range(n)]
  for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
      b[i] -= a[i][j] * x[j]
    x[i] = b[i] / a[i][i]
  return x

def triangularInferior(a, b, n):
  x = [0 for _ in range(n)]
  for i in range(n):
    for j in range(i):
      b[i] -= a[i][j] * x[j]
    x[i] = b[i] / a[i][i]
  return x

def solveLU(a, b, n):
  l,u,swp = fatLU(a, n)
  for (i,j) in swp:
    b[i], b[j] = b[j], b[i]
  y = triangularInferior(l, b, n)
  x = triangularSuperior(u, y, n)
  return x

def solveCholesky(a, b, n):
  for i in range(n):
    for j in range(i, n):
      if a[i][j] != a[j][i]:
        return None
  l,u,swp = fatLU(a, n)
  for (i,j) in swp:
    b[i], b[j] = b[j], b[i]
  for i in range(n):
    if u[i][i] < 0:
      return None
  uu = id(n)
  for i in range(n):
    uu[i][i] = sqrt(u[i][i])
  g = prod(l, uu, n)
  _g = transpose(g, n)
  y = triangularInferior(g, b, n)
  x = triangularSuperior(_g, y, n)
  return x


