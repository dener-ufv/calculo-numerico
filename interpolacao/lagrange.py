def L(k, x, vx, n):
  pr = 1
  for i in range(n):
    if(i != k):
      pr *= (x-vx[i]) / (vx[k] - vx[i])
  return pr

def Pn(x, vx, vy, n):
  ans = 0
  for i in range(n):
    ans += L(i, x, vx, n)*vy[i]
  return ans

vx = [-1, 0, 3]
vy = [15, 8, -1]
n = 3
x = 1

print(Pn(x, vx, vy, n))
