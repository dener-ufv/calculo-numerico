def F(x, fx):
  return 1 / x * (2*fx + x + 1)

x0 = 1
y0 = 0.5
end = 2
h = 0.2

while True:
  print(x0, y0)
  if(abs(x0 - end) < 0.000001):
    break
  y0 = y0 + F(x0, y0)*h
  x0 += h


