from sys import stdin
from collections import deque
input = lambda : stdin.readline().strip()

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))
queue = deque()
queue.append(((0, 0), 1, False))
graph[0][0] = -1
while queue:
    node = queue.popleft()
    if node[0] == (m - 1, n - 1):
        break
    for i, j in zip([-1, 0, 1, 0], [0, -1, 0, 1]):
        new_x, new_y = node[0][0] + i, node[0][1] + j
        if 0 <= new_x < m and 0 <= new_y < n:
            if node[2]:
                if graph[new_y][new_x] == 0:
                    queue.append(((new_x, new_y), node[1] + 1, node[2]))
                    graph[new_y][new_x] = 2
            else:
                if graph[new_y][new_x] >= 0:
                    if graph[new_y][new_x] == 1:
                        queue.append(((new_x, new_y), node[1] + 1, True))
                    else:
                        queue.append(((new_x, new_y), node[1] + 1, node[2]))
                    graph[new_y][new_x] = -1
if node[0] == (m - 1, n - 1):
    print(node[1])
else:
    print(-1)