n, m = map(int, input().split())
board = list()
for i in range(n):
	board.append(list(input()))

min = n * m
for i in range(n - 7):
	for j in range(m - 7):
		count = 0
		count2 = 0
		for k in range(i, i + 8):
			for w in range(j, j + 8):
				if k == i and w == j:
					toFind = board[k][w]
					pass
				if (k + w) % 2:
					if board[k][w] == toFind:
						count += 1
					else:
						count2 += 1
				else:
					if board[k][w] != toFind:
						count += 1
					else:
						count2 += 1
		if count < min:
			min = count
		if count2 < min:
			min = count2
print(min)