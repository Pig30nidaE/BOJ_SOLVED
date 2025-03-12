from sys import stdin
from collections import deque
input = lambda : stdin.readline()

n = int(input())
rec = []
for _ in range(n):
    rec.append(list(map(int," ".join(input()).split())))
visited = set()
counter = []
house = 0
chk = [[1, 0, -1, 0], [0, 1, 0, -1]]
for i in range(n):
    for j in range(n):
        if rec[i][j] and (i, j) not in visited:
            house += 1
            visited.add((i, j))
            queue = deque()
            queue.append((i, j))
            count = 1
            while queue:
                node = queue.popleft()
                for row, col in zip(chk[0], chk[1]):
                    new_y, new_x = node[0] + row, node[1] + col
                    if 0 <= new_x < n and 0 <= new_y < n:
                        if rec[new_y][new_x] and (new_y, new_x) not in visited:
                            queue.append((new_y, new_x))
                            visited.add((new_y, new_x))
                            count += 1
            counter.append(count)
print(house)
for i in sorted(counter):
    print(i)
