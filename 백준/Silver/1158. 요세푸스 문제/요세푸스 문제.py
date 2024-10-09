from sys import stdin
from collections import deque
input = lambda : stdin.readline().strip()

n, k = map(int, input().split())

people = deque(i for i in range(1, n + 1))

print('<', end='')
while people:
    for _ in  range(k - 1):
        people.rotate(-1)
    if len(people) == 1:
        print(f'{people.popleft()}>')
    else:
        print(f'{people.popleft()},', end=' ')