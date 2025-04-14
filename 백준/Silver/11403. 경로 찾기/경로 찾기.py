from sys import stdin
from collections import defaultdict, deque
input = lambda : stdin.readline()

n = int(input())
info = [0] * n
graph = defaultdict(list)
for i in range(n):
    info[i] = list(map(int, input().split()))
    for j in range(n):
        if info[i][j]:
            graph[i].append(j)

answer = [[0] * n for _ in range(n)]
# dp = defaultdict(set)

for i in range(n):
    queue = deque()
    visited = set()
    node = i
    queue.append(node)
    visited.add(node)
    while queue:
        node = queue.popleft()
        for j in graph[node]:
            if j not in visited:
                queue.append(j)
                visited.add(j)
                answer[i][j] = 1
            else:
                if j == i:
                    answer[i][j] = 1


for i in answer:
    for j in i:
        print(j, end=' ')
    print()



    