def F(x, fx):
  return fx * (x*x - 1)

def heun(x0, y0, h, end, e):
  x = x0
  y = y0
  while abs(x-end) >= e:
    y = y + h/2*(F(x, y) + F(x+h, y + h*F(x, y)))
    x += h
    print(x, y)
  return y


print(heun(0, 1, 0.5, 1, 0.000001))
