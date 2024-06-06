from sys import stdin
input = stdin.readline

t = int(input())
for testcase in range(1, t + 1):
	n = int(input())
	x, y = list(), list()
	for _ in range(n):
		tmp1, tmp2 = map(float, input().split())
		x.append(tmp1)
		y.append(tmp2)
	width = max(x) - min(x)
	height = max(y) - min(y)
	print(f'Case {testcase}: Area {width * height}, Perimeter {height * 2 + width * 2}')