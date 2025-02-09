from collections import deque
from sys import stdin
input = lambda : stdin.readline().strip()


def bfs(start: list, campus: list, n: int, m: int) -> int:
	queue = deque()
	queue.append(start)
	visited = {start}
	count = 0
	while queue:
		node = queue.popleft()
		for i, j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
			new_y, new_x = node[0] + i, node[1] + j
			if 0 <= new_y < n and 0 <= new_x < m:
				if (new_y, new_x) not in visited and campus[new_y][new_x] in ('O', 'P'):
					queue.append((new_y, new_x))
					visited.add((new_y, new_x))
					if campus[new_y][new_x] == 'P':
						count += 1
	return count
	

if __name__ == '__main__':
	n, m = map(int, input().split())
	campus = []
	for i in range(n):
		campus.append(list(input()))
		for j in range(m):
			if campus[i][j] == 'I':
				start = (i, j)
	res = bfs(start, campus, n, m)
	if not res:
		print('TT')
	else:
		print(res)