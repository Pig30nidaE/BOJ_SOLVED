from sys import stdin
input = stdin.readline

def markCctvRange(toMark: list, info: list, idx: tuple)->int:
	global n, m
	to_sub = 0
	new_x, new_y = idx[0] + info[0], idx[1] + info[1]
	while 0 <= new_x < n and 0 <= new_y < m and toMark[new_x][new_y] != 6:
		if toMark[new_x][new_y] == 0:
			to_sub += 1
			toMark[new_x][new_y] = -1
		new_x += info[0]
		new_y += info[1]
	return to_sub

def recur(board: list, depth: int, blindSpot: int)->int:
	global cctv_list, n, m
	if depth == len(cctv_list):
		return blindSpot
	idx = (cctv_list[depth][0], cctv_list[depth][1])
	cctv_type = board[idx[0]][idx[1]]
	firstBlindSpot = blindSpot
	if cctv_type == 1:
		for i, j in zip([1, 0, -1, 0], [0, 1, 0, -1]):
			to_sub = 0
			board_copy = [arr[:] for arr in board]
			to_sub += markCctvRange(board_copy, (i, j), idx)
			num = recur(board_copy, depth + 1, blindSpot - to_sub)
			if firstBlindSpot > num:
				firstBlindSpot = num
		return firstBlindSpot
	elif cctv_type == 2:
		for i, j in zip([1, 0], [0, 1]):
			to_sub = 0
			board_copy = [arr[:] for arr in board]
			to_sub += markCctvRange(board_copy, (i, j), idx)
			to_sub += markCctvRange(board_copy, (-i, -j), idx)
			num = recur(board_copy, depth + 1, blindSpot - to_sub)
			if firstBlindSpot > num:
				firstBlindSpot = num
		return firstBlindSpot
	elif cctv_type == 3:
		for i, j in zip([1, -1, -1, 1], [1, 1, -1, -1]):
			to_sub = 0
			board_copy = [arr[:] for arr in board]
			to_sub += markCctvRange(board_copy, (i, 0), idx)
			to_sub += markCctvRange(board_copy, (0, j), idx)
			num = recur(board_copy, depth + 1, blindSpot - to_sub)
			if firstBlindSpot > num:
				firstBlindSpot = num
		return firstBlindSpot
	elif cctv_type == 4:
		for i in range(4):
			to_sub = 0
			board_copy = [arr[:] for arr in board]
			if i == 0:
				to_sub += markCctvRange(board_copy, (-1, 0), idx)
				to_sub += markCctvRange(board_copy, (0, 1), idx)
				to_sub += markCctvRange(board_copy, (0, -1), idx)
			elif i == 1:
				to_sub += markCctvRange(board_copy, (-1, 0), idx)
				to_sub += markCctvRange(board_copy, (1, 0), idx)
				to_sub += markCctvRange(board_copy, (0, 1), idx)
			elif i == 2:
				to_sub += markCctvRange(board_copy, (0, 1), idx)
				to_sub += markCctvRange(board_copy, (1, 0), idx)
				to_sub += markCctvRange(board_copy, (0, -1), idx)
			else:
				to_sub += markCctvRange(board_copy, (1, 0), idx)
				to_sub += markCctvRange(board_copy, (-1, 0), idx)
				to_sub += markCctvRange(board_copy, (0, -1), idx)

			num = recur(board_copy, depth + 1, blindSpot - to_sub)
			if firstBlindSpot > num:
				firstBlindSpot = num
		return firstBlindSpot
	elif cctv_type == 5:
		to_sub = 0
		board_copy = [arr[:] for arr in board]
		for i, j in zip([1, 0, -1, 0], [0, 1, 0, -1]):
			to_sub += markCctvRange(board_copy, (i, j), idx)
		return recur(board_copy, depth + 1, blindSpot - to_sub)

n, m = map(int, input().split())
board = list()
cctv_list = list()
firstBlindSpot = 0
for i in range(n):
	board.append(list(map(int, input().split())))
	for j in range(m):
		if 1 <= board[i][j] <= 5:
			cctv_list.append((i, j))
		elif board[i][j] == 0:
			firstBlindSpot += 1

print(recur(board, 0, firstBlindSpot))
