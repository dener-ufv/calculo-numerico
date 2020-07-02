import math
from function import *

# intervalo = [l, r] 
# precisao  = e
def bissecao(l, r, e):
  while True:
    x = (l+r)/2
    res = func(x)
    if abs(res) < e:
      break
    if res*func(l) < 0:
      r = x
    elif res*func(r) < 0:
      l = x
  return x

# ponto inicial = l
# ponto final   = r
# precisao      = e
def posicaoFalsa(l, r, e):
  while True:
    x = (l*func(r) - r*func(l)) / (func(r) - func(l))
    res = func(x)
    if abs(res) < e:
      break
    if res*func(l) < 0:
      r = x
    elif res*func(r) < 0:
      l = x
  return x

# x0
# x1
# precisao = e
def secante(x0, x1, e):
  while True:
    x = (x0*func(x1) + x1*func(x0)) / (func(x1) - func(x0))
    res = func(x)
    if abs(res) < e :
      break
    x0 = x1
    x1 = x
  return x


# x
# precisao e
def newtonHapson(x, e):
  while True:
    res = func(x)
    if abs(res) < e:
      break
    x -= func(x) / deriv(x)
  return x
