from math import ceil

a, b, v = map(int, input().split())

sub = a - b
count = ceil((v - a)/sub)
print(count + 1)