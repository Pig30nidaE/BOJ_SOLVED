from sys import stdin
from collections import deque
input = stdin.readline

t = int(input())
for _ in range(t):
	count = 0
	n, m = map(int, input().split())
	queue = deque(map(int, input().split()))
	priority = deque(sorted(queue, reverse=True))
	for i in range(n):
		queue[i] = (queue[i], i)
	while queue[0][1] != m or queue[0][0] != priority[0]:
		if queue[0][0] == priority[0]:
			queue.popleft()
			priority.popleft()
			count += 1
		else:
			queue.rotate(-1)
	print(count + 1)
