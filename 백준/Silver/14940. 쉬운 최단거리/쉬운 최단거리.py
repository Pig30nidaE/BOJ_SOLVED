from collections import deque
from sys import stdin
input = stdin.readline


n, m = map(int, input().split())
board = list()
loc_flag = False
dest = tuple()
for i in range(n):
	board.append(list(map(int, input().split())))
	if not loc_flag:
		for j in range(m):
			if board[i][j] == 2:
				dest = (i, j)
				loc_flag = True
visited = set()
queue = deque()
count = 0
x_dir = [-1, 0, 1, 0]
y_dir = [0, 1, 0, -1]
queue.append(dest)
visited.add(dest)
board[dest[0]][dest[1]] = 0
while len(queue):
	start = queue.popleft()
	for i, j in zip(y_dir, x_dir):
		to_y = start[0] + i
		to_x = start[1] + j
		if 0 <= to_y < n and 0 <= to_x < m:
			if board[to_y][to_x] == 1:
				if (to_y, to_x) not in visited:
					queue.append((to_y, to_x))
					visited.add((to_y, to_x))
					board[to_y][to_x] = board[start[0]][start[1]] + 1

for i in range(n):
	for j in range(m):
		if (i, j) not in visited and board[i][j] == 1:
			print(-1, end=" ")
		else:
			print(board[i][j], end=" ")
	print()
				

