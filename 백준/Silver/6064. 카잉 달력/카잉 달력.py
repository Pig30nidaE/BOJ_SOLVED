from sys import stdin, stdout
input = lambda: stdin.readline()
print = stdout.write
t = int(input())


for _ in range(t):
    m, n, x, y = map(int, input().split())
    lim = min(m * n, 2147483647)
    numset = set()

    flag = False
    while x <= lim or y <= lim:
        if x in numset:
            print(f'{x}\n')
            flag = True
            break
        numset.add(x)
        if y in numset:
            print(f'{y}\n')
            flag = True
            break
        numset.add(y)
        x += m
        y += n
    if not flag:
        print('-1\n')