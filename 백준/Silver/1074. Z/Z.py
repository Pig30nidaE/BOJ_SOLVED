from sys import setrecursionlimit, stdin, stdout
setrecursionlimit(100000000)
input = stdin.readline
count = 0
def recur(depth: int, x: int, y: int):
	global r, c, flag, count
	if depth == 0:
		if x == c and y == r:
			print(count)
		elif x + 1 == c and y == r:
			print(count + 1)
		elif x == c and y + 1 == r:
			print(count + 2)
		elif x + 1 == c and y + 1 == r:
			print(count + 3)
		else:
			print(count + 4)
		exit()
	x_flag = False
	y_flag = False
	flag = False
	if x + 2 ** depth <= c:
		x_flag = True
	if y + 2 ** depth <= r:
		y_flag = True
	if x_flag and y_flag:
		flag = True
	if flag:
		x += 2 ** depth
		y += 2 ** depth
		count += ((4 ** depth) * 3)
	else:
		if not x_flag and y_flag:
			count += ((4 ** depth) * 2)
			y += 2 ** depth
		elif x_flag and not y_flag:
			count += (4 ** depth)
			x += 2 ** depth
		else:
			depth -= 1
	recur(depth, x, y)


n, r, c = map(int, input().split())
recur(n - 1, 0, 0)