from sys import stdin
input = lambda : stdin.readline().strip()


m, n = map(int, input().split())

count = 0
corner = 0
last = m * n
flag = False
while count != last:
    if not flag:
        flag = True
        count += n
        n -= 1
    else:
        flag = False
        m -= 1
        count += m
    corner += 1
print(corner - 1)