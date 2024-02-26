import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000000)



color_dict = dict()
color_dict[0] = 0
color_dict[1] = 0

def check(board: list, check_num: int, x: int, y: int)->bool:
	global color_dict
	color = board[y][x]
	for i in range(y, y + check_num):
		for j in range(x, x + check_num):
			if board[i][j] != color:
				return False
	color_dict[color] += 1
	return True

def recur(n: int, board: list, x: int, y: int):
	if not check(board, n, x, y):
		recur(n // 2, board, x, y)
		recur(n // 2, board, x + n // 2, y)
		recur(n // 2, board, x, y + n // 2)
		recur(n // 2, board, x + n // 2, y + n // 2)



n = int(input())
board = list()
for _ in range(n):
	board.append(list(map(int, input().split())))

recur(n, board, 0, 0)
for i in color_dict.values():
	print(i)