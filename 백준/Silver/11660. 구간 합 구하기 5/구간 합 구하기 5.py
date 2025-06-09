from sys import stdin
input = stdin.readline


def solve():
	n, m = map(int, input().split())
	dp = [[0] + list(map(int, input().split())) for _ in range(n)]
	dp.insert(0, [0] * (n + 1))
	
	for i in range(2, n + 1):
		dp[1][i] += dp[1][i - 1]
	for i in range(2, n + 1):
		dp[i][1] += dp[i - 1][1]
		for j in range(2, n + 1):
			dp[i][j] = dp[i][j - 1] + dp[i - 1][j] + dp[i][j] - dp[i - 1][j - 1]

	for _ in range(m):
		x1, y1, x2, y2 = map(int, input().split())
		print(dp[x2][y2] - dp[x2][y1 - 1] - dp[x1 - 1][y2] + dp[x1 - 1][y1 - 1])

if __name__ == '__main__':
	solve()