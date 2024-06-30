from sys import stdin
input = stdin.readline

colors = list()
for _ in range(16):
	colors.append(list(map(int, input().split())))

rgb = list(map(int, input().split()))
while rgb[0] != -1:
	min_d = 256 ** 2 + 256 ** 2 + 256 ** 2
	memo = [0, 0, 0]
	for i in colors:
		calc = (i[0] - rgb[0]) ** 2 + (i[1] - rgb[1]) ** 2 + (i[2] - rgb[2]) ** 2
		if calc < min_d:
			min_d = calc
			memo = i
	print(f'({rgb[0]},{rgb[1]},{rgb[2]}) maps to ({memo[0]},{memo[1]},{memo[2]})')
	rgb = list(map(int, input().split()))
