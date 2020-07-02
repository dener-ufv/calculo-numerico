def verifyPrecision(prevx, x, n, e):
  maxd = 0
  maxv = 0
  for i in range(n):
    maxd = max(maxd, abs(x[i] - prevx[i]))
    maxv = max(maxv, abs(x[i]))
  print(maxd/maxv)
  return (maxd < maxv*e)


def gauussSeidel(a, b, x, n):
  newx = [x[i] for i in range(n)]
  for i in range(n):
    newx[i] = 0
    for j in range(n):
      if i == j:
        newx[i] += b[i] / a[i][i]
      else:
        newx[i] -= newx[j] * a[i][j] / a[i][i]
  return newx

def verifyConvergence(a, n):
  s = [1 for _ in range(n)]
  for i in range(n):
    s[i] = 0
    for j in range(n):
      if i != j:
        s[i] += abs(a[i][j]) * s[j] / abs(a[i][i])
    if s[i] >= 1:
      return False
  return True

def solve(a, b, x, n, e):
  while True:
    newx = gauussSeidel(a, b, x, n)
    if verifyPrecision(x, newx, n, e):
      break
    x = newx
  return newx



a = [[1,1,0,2], [1,2,-2,0], [0,-2,5,1], [2,0,1,18]]
b = [1,1,1,1]
x = [0,0,0,0]
n = 4
e = 0.0005
solve(a,b,x,n,e)
#print(solve(a, b, x, n, e))
