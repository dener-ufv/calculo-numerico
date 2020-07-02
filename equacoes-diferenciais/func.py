def func(x, fx, h):
  return fx * (1 + (x*x - 1)*h)

x0, y0, end = map(float, input().split())

while abs(x0 - end) >= 0.000001:
  print(func(x0, y0, 0.5))
  y0 = func(x0, y0, 0.5)
  x0 += 0.5


