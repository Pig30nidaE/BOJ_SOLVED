from sys import stdin
input = stdin.readline

n, g = map(int, input().split())

rooms = [0 for _ in range(n)]
groups = list()

for i in range(g):
	groups.append(int(input()))

rooms_idx = 0
for i in range(g):
	while groups[i] >= 2 and rooms_idx < n:
		rooms[rooms_idx] += 2
		groups[i] -= 2
		rooms_idx += 1
	if groups[i] and rooms_idx < n:
		rooms[rooms_idx] += 1
		rooms_idx += 1
		groups[i] -= 1
rooms_idx = 0
for i in groups:
	while rooms_idx < n:
		if i:
			if rooms[rooms_idx] == 1:
				rooms[rooms_idx] += 1
				i -= 1
		rooms_idx += 1
	if rooms_idx == n:
		rooms_idx = 0
for i in rooms:
	print(i)