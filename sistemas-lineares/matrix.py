def id(n):
  m = [[0 for _ in range(n)] for __ in range(n)]
  for i in range(n):
    m[i][i] = 1.0
  return m

def prod(ma, mb, n):
  m = [[0 for _ in range(n)] for __ in range(n)]
  for i in range(n):
    for j in range(n):
      s = 0
      for k in range(n):
        s += ma[i][k] * mb[k][j]
      m[i][j] = s
  return m

def printM(m, n):
  for i in range(n):
    print(*m[i])

def transpose(m, n):
  return [[m[i][j] for i in range(n)] for j in range(n)]
