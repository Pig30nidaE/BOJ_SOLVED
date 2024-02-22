from collections import deque
import sys
input = sys.stdin.readline


n, m = map(int, input().split())
if not m:
	print(n)
	exit()
node = dict()
for _ in range(m):
	n1, n2 = map(int, input().split())
	try:
		node[n1].append(n2)
	except KeyError:
		node[n1] = [n2]
	try:
		node[n2].append(n1)
	except KeyError:
		node[n2] = [n1]


queue = deque()
visited = set()
count = 0
for i in node.keys():
	if i not in visited:
		count += 1
		visited.add(i)
		queue.append(i)
		while len(queue):
			#print(queue)
			start = queue.popleft()
			for j in node[start]:
				if j not in visited:
					queue.append(j)
					visited.add(j)

count += n - len(node.keys())
print(count)
