from sys import stdin
input = stdin.readline



def solution():
	t = int(input())
	ans = []
	for _ in range(t):
		n = int(input())
		stickers = []
		for _ in range(2):
			stickers.append(list(map(int, input().split())))
		if n == 1:
			print(max(stickers[0][0], stickers[1][0]))
			continue
		dp = [[0] * n for _ in range(2)]
		dp[0][0] = stickers[0][0]
		dp[1][0] = stickers[1][0]

		dp[0][1] = dp[1][0] + stickers[0][1]
		dp[1][1] = dp[0][0] + stickers[1][1]

		for i in range(2, n):
			dp[0][i] = max(dp[1][i - 1], dp[1][i - 2]) + stickers[0][i]
			dp[1][i] = max(dp[0][i - 1], dp[0][i - 2]) + stickers[1][i]
		ans.append(max(dp[0][-1], dp[1][-1]))
	for a in ans:
		print(a)
if __name__ == '__main__':
	solution()