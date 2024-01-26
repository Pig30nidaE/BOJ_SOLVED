import math
fac = math.factorial

n, k = map(int, input().split())
print(int(fac(n)/(fac(k)*fac(n-k))))
