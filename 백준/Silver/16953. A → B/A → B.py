from collections import deque

a, b = map(int, input().split())
queue = deque()
queue.append((a, 0))
visited = {a}

while queue:
	node = queue.popleft()
	if node[0] == b:
		print(node[1] + 1)
		break
	if node[0] > b:
		continue
	multiply = node[0] * 2
	plus = node[0] * 10 + 1
	if multiply not in visited:
		queue.append((multiply, node[1] + 1))
		visited.add(multiply)
	if plus not in visited:
		queue.append((plus, node[1] + 1))
		visited.add(plus)
if not queue:
	print(-1)