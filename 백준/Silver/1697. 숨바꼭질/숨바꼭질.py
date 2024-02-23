from collections import deque

n, m = map(int, input().split())
board = [0 for i in range(2 * m)]

def update_board(n: int, after_move: int, board: list):
	if not board[after_move] or board[after_move] > board[n] + 1:
		queue.append(after_move)
		board[after_move] = board[n] + 1

if n >= m:
	print(n - m)
else:
	queue = deque()
	queue.append(n)
	while queue:
		start = queue.popleft()
		if start == m:
			print(board[start])
			break
		if 0 < start * 2 <= 2 * m:
			update_board(start, start * 2, board)
		if 0 < start - 1 <= 2 * m:
			update_board(start, start - 1, board)
		if 0 < start + 1 <= 2 * m:
			update_board(start, start + 1, board)