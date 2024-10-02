from sys import stdin
from collections import deque
from string import ascii_lowercase, ascii_uppercase
input = lambda : stdin.readline().strip()


lower = dict()
upper = dict()
idx = 1
for i in ascii_uppercase:
    upper[i] = idx
    idx += 1
idx = 1
for i in ascii_lowercase:
    lower[i] = idx
    idx += 1

ndigit = deque(input())
patterns = input()

ans = 0
try:
    for i in patterns:
        if i in lower.keys():
            for _ in range(lower[i]):
                ans += int(ndigit.popleft())
        else:
            for _ in range(upper[i]):
                ndigit.popleft()
    if ndigit:
        print('non sequitur')
    else:
        print(ans)
except IndexError:
    print('non sequitur')