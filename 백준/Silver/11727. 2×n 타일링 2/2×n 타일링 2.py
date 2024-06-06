dp = dict()
def recur(n : int)->int:
	if n == 1:
		return 1
	elif n == 2:
		return 3
	else:
		if n not in dp.keys():
			dp[n] = 2 * recur(n - 2) + recur(n - 1)
		return dp[n]


n = int(input())
print(recur(n) % 10007)