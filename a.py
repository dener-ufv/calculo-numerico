def f(prevy, h):
  return prevy * (1 + 5*h + 25*h*h/2 + 125*h*h*h/6)


x = 0
y = 1
h = 0.01
for i in range(10):
  y = f(y, h)
  x += h
  print(x, y)
