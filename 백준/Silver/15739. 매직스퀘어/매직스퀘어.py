from sys import stdin
input = stdin.readline

n = int(input())
tmp = list()
for i in range(n):
	tmp.append(list(map(int, input().split())))

for i in range(n):
	check_set = set(tmp[i])
	if len(check_set) != n:
		print("FALSE")
		exit()

check = n * (n ** 2 + 1) // 2
for i in range(n):
	if sum(tmp[i]) != check:
		print("FALSE")
		exit()
for i in range(n):
	res = 0
	for j in range(n):
		res += tmp[j][i]
	if res != check:
		print("FALSE")
		exit()
res = 0
for i, j in zip(range(n), range(n)):
	res += tmp[i][j]
if res != check:
	print("FALSE")
	exit()
res = 0
for i, j in zip(range(n), range(n - 1, -1, -1)):
	res += tmp[i][j]
if res != check:
	print("FALSE")
	exit()
print("TRUE")