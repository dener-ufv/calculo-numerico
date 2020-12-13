def gcd(a, b):
  if b == 0:
    return a
  return gcd(b, a%b)

print("a/b")
a,b = map(int, input().split())
print(a//gcd(a, b), "/", b//gcd(a, b))
