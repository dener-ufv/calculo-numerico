import math

def f(x):
  return math.exp(x) * math.cos(x)

def integral(x0, xn, h):
  res = 0
  while abs(xn - x0) >= 0.000001:
    res += f(x0) + 3*f(x0+h) + 3*f(x0+2*h) + f(x0+3*h)
    x0 += 3*h
  return res*h*3/8

print(integral(0, 1.2, 0.2))
