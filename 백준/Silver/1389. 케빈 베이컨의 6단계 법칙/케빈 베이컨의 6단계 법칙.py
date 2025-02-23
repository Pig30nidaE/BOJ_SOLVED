from sys import stdin
from collections import deque
input = stdin.readline

n, m = map(int, input().split())


graph = dict()
for _ in range(m):
	a, b = map(int, input().split())
	if a in graph.keys():
		graph[a].append(b)
	else:
		graph[a] = [b]
	if b in graph.keys():
		graph[b].append(a)
	else:
		graph[b] = [a]


min = 10 ** 7
last = []
for i in range(1, n + 1):
	queue = deque()
	queue.append(i)
	visited = set()
	bacon = [0 for _ in range(n)]
	count = 0
	while queue:
		node = queue.popleft()
		visited.add(node)
		for j in graph[node]:
			if j not in visited:
				queue.append(j)
				visited.add(j)
				bacon[j - 1] = bacon[node - 1] + 1
	res = sum(bacon)
	if res < min:
		min = res
		last = [i]
	if res == min:
		last.append(i)
print(sorted(last)[0])
