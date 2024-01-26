from sys import setrecursionlimit
setrecursionlimit(100000000)

def fibonnaci(n: int, dp: list)->list:
	if n == 0:
		dp[0][0] = 1
		return [1, 0]
	elif n == 1:
		dp[1][1] = 1
		return [0, 1]
	else:
		#print(dp)
		if dp[n - 1][0] or dp[n - 1][1]:
			res = dp[n - 1]
		else:
			res = fibonnaci(n - 1, dp)
		if dp[n - 2][0] or dp[n - 2][1]:
			res2 = dp[n - 2]
		else:
			res2 = fibonnaci(n - 2, dp)
		dp[n][0] = res[0] + res2[0]
		dp[n][1] = res[1] + res2[1]
		return dp[n]

if __name__ == '__main__':
	import sys
	input = sys.stdin.readline
	n = int(input())
	for i in range(n):
		num = int(input())
		dp = [[0, 0] for _ in range(num + 1)]
		res = fibonnaci(num, dp)
		print(f'{res[0]} {res[1]}')