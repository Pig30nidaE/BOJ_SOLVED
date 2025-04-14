from sys import stdin
from collections import deque
input = lambda : stdin.readline()

n, m = map(int, input().split())
move = dict()
for _ in range(n):
    start, end = map(int, input().split())
    move[start] = end
for _ in range(m):
    start, end = map(int, input().split())
    move[start] = end

queue = deque()
queue.append((1, 0))
visited = set()
visited.add(1)
loc, count = 0, 1
while queue:
    node = queue.popleft()
    if node[loc] == 100:
        print(node[count])
        break
    for i in range(1, 7):
        if node[loc] + i not in visited:
            if node[loc] + i in move.keys():
                new_node = (move[node[loc] + i], node[count] + 1)
            else:
                new_node = (node[loc] + i, node[count] + 1)
            queue.append(new_node)
            visited.add(node[loc] + i)

