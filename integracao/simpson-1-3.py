import math

def f(x):
  return math.exp(x) * math.cos(x)

def integral(x0, xn, h):
  res = 0
  while abs(xn - x0) >= 0.000001:
    res += f(x0) + 4*f(x0+h) + f(x0+2*h)
    x0 += 2*h
  return res*h/3

print(integral(0, 1.2, 0.2))
