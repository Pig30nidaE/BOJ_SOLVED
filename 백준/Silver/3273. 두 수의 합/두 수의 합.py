from sys import stdin
input = lambda : stdin.readline().strip()


n = int(input())
seq = sorted(list(map(int, input().split())))
x = int(input())

count = 0
pt1 = 0
pt2 = n - 1
while pt1 != pt2:
    sum = seq[pt1] + seq[pt2]
    if sum <= x:
        if sum == x:
            count += 1
        pt1 += 1
    else:
        pt2 -= 1
print(count)