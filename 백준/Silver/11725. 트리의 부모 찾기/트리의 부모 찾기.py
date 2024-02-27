from collections import deque
import sys
input = sys.stdin.readline
n = int(input())

tree = dict()
for i in range(n - 1):
	v1, v2 = map(int, input().split())
	try:
		tree[v1].append(v2)
	except KeyError:
		tree[v1] = [v2]
	try:
		tree[v2].append(v1)
	except KeyError:
		tree[v2] = [v1]

queue = deque()
queue.append(1)
new_tree = dict()
visited = set()
while queue:
	node = queue.popleft()
	visited.add(node)
	try:
		for i in tree[node]:
			if i not in visited:
				new_tree[i] = node
				queue.append(i)
	except KeyError:
		pass
for i in range(2, n + 1):
	print(new_tree[i])
