from sys import stdin
from collections import deque
input = stdin.readline


visited = set()
def dfs(node: dict, curr: int):
	print(curr, end=' ')
	if curr not in node.keys():
		return
	visited.add(curr)
	for i in node[curr]:
		if i not in visited:
			dfs(node, i)
	return

def bfs(node: dict, v: int):
	queue = deque()
	queue.append(v)
	visited.add(v)
	while queue:
		curr = queue.popleft()
		print(curr, end=' ')
		if curr in node.keys():
			for pt in node[curr]:
				if pt not in visited:
					queue.append(pt)
					visited.add(pt)

def main():
	n, m, v = map(int, input().split())
	node = dict()
	for _ in range(m):
		pt1, pt2 = map(int, input().split())
		try:
			node[pt1].append(pt2)
		except KeyError:
			node[pt1] = [pt2]
		try:
			node[pt2].append(pt1)
		except KeyError:
			node[pt2] = [pt1]
	for value in node.values():
		value.sort()
	dfs(node, v)
	visited.clear()
	print()
	bfs(node, v)

if __name__ == '__main__':
	main()