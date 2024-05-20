from sys import stdin
input = stdin.readline

t = int(input())
for i in range(t):
	k = int(input())
	n = int(input())
	downstair = [j for j in range(1, n + 1)]
	upstair = [0 for j in range(n)]
	for j in range(1, k + 1):
		for w in range(n):
			upstair[w] = sum(downstair[0:w + 1])
		downstair = upstair.copy()
	print(upstair[-1])