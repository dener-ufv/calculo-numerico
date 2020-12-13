import math

def f(x):
  return x * math.exp(x) * math.cos(x)

def integral(x0, xn, h):
  res = 0
  while abs(xn - x0) >= 0.0000001:
    res += f(x0) + f(x0+h)
    x0 += h
  return res*h/2

print(integral(0, 1.2, 0.1))
