from sys import stdin
input = stdin.readline

n = int(input())
stairs = list()
for _ in range(n):
    stairs.append(int(input()))

dp = dict()
dp[0] = stairs[0]
if n > 1:
    dp[1] = stairs[1] + dp[0]
if n > 2:
    dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

for i in range(len(dp.keys()), n):
    dp[i] = max(dp[i - 2] + stairs[i], dp[i - 3] + stairs[i - 1] + stairs[i])

print(dp[n - 1])