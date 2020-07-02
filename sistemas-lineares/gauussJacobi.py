def verifyPrecision(prevx, x, n, e):
  maxd = 0
  maxv = 0
  for i in range(n):
    maxd = max(maxd, abs(x[i] - prevx[i]))
    maxv = max(maxv, abs(x[i]))
  return (maxd < maxv*e)


def gauussJacobi(a, b, x, n):
  newx = [0 for _ in range(n)]
  for i in range(n):
    for j in range(n):
      if i == j:
        newx[i] += b[i] / a[i][i]
      else:
        newx[i] -= x[j] * a[i][j] / a[i][i]
  return newx

def verifyConvergence(a, n):
  for i in range(n):
    s = 0 
    for j in range(n):
      if i != j:
        s += abs(a[i][j]) / abs(a[i][i])
    if s >= 1:
      return False
  return True

def solve(a, b, x, n, e):
  cnt = 3
  while cnt > 0:
    cnt -= 1
    newx = gauussJacobi(a, b, x, n)
    #if verifyPrecision(x, newx, n, e):
    #  break
    x = newx
    print(newx)
  return newx



a = [[1,1,0,2], [1,2,-2,0], [0,-2,5,1], [2,0,1,18]]
b = [1,1,1,1]
x = [0,0,0,0]
n = 4
e = 0.0005
print(solve(a, b, x, n, e))
