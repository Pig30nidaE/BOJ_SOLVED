from sys import stdin
input = stdin.readline


n = int(input())
if n == 1:
	print(1)
	exit()
if n == 2:
	print(1)
	exit()

dp = dict()

dp[2] = (1, 0)

for i in range(3, n):
	num = dp[i - 1]
	dp[i] = (num[0] + num[1], num[0])
		#if num[-1] == '0':
		#	dp[i].append(num + '0')
		#	dp[i].append(num + '1')
		#else:
		#	dp[i].append(num + '0')

num = dp[n - 1]
dp[n] = (num[0] + num[1], num[0])
print(dp[n][0] + dp[n][1])