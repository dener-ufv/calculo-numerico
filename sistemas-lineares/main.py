from solution import *

print("size: ", end="")
n = int(input())
print("A:")
a = [list(map(float, input().split())) for _ in range(n)]

l, u, swp = fatLU(a, n)
print(l)
print()
print(u)
