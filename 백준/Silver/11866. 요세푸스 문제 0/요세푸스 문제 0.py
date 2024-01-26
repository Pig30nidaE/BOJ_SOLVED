from collections import deque
n, k = map(int, input().split())
table = deque(i for i in range(1, n + 1))
print("<", end="")
for i in range(n):
	table.rotate(-k+1)
	if i == n - 1:
		print(table.popleft(), end=">")
	else:
		print(table.popleft(), end=", ")
