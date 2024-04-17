from sys import stdin
input = stdin.readline


n = int(input())
consumer = list()
for i in range(n):
	consumer.append(tuple(map(int, input().split())))

dp = dict()

def recur(idx: int, n: int, sum: int, consumer: list)->int:
	if idx >= n:
		return 0
	if idx in dp.keys():
		return dp[idx]
	max = 0
	for i in range(idx, n):
		if consumer[idx][0] + i <= n:
			res = recur(i + consumer[idx][0], n, sum + consumer[idx][1], consumer)
			if res + consumer[idx][1] > max:
				max = res + consumer[idx][1]
	dp[idx] = sum + max
	return dp[idx]


for i in range(n - 1, -1, -1):
	recur(i, n, 0, consumer)
print(max(dp.values()))