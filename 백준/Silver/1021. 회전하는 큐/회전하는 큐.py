from sys import stdin
from collections import deque
input = lambda : stdin.readline().strip()

n, m = map(int, input().split())
seq = deque(i for i in range(1, n + 1))
topop = list(map(int, input().split()))
count = 0
for num in topop:
    idx = 0
    while seq[idx % n] != num:
        idx += 1
    idx2 = 0
    while seq[-(idx2 % n)] != num:
        idx2 += 1
    if idx < idx2:
        seq.rotate(-idx)
        seq.popleft()
        count += idx
    else:
        seq.rotate(idx2)
        seq.popleft()
        count += idx2
print(count)