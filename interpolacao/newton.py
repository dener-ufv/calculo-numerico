def D(vx, vy, n):
  d = [[0 for i in range(n)] for j in range(n)]
  for j in range(n):
    for i in range(n-j):
      if j == 0:
        d[i][j] = vy[i]
      else:
        d[i][j] = (d[i+1][j-1] - d[i][j-1]) / (vx[i+j] - vx[i])
  return [d[0][j] for j in range(n)]

def Pn(x, vx, vy, n):
  ans=0
  d = D(vx, vy, n)
  for i in range(n):
    pr = d[i]
    for j in range(i):
      pr *= (x-vx[j])
    ans += pr
  return ans



vx = [-1, 0, 1, 2]
vy = [29, 30, 31, 62]
n = 4
x = 1.5
print(Pn(x, vx, vy, n))
