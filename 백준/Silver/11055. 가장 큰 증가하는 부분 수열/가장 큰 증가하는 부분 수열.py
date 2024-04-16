from sys import stdin
input = stdin.readline


n = int(input())
nums = list(map(int, input().split()))

dp = dict()

def recur(idx: int, n: int, sum: int, nums: list)->int:
	global dp
	if idx in dp.keys():
		return dp[idx]
	max = 0
	for i in range(idx + 1, n):
		if nums[i] > nums[idx]:
			res = recur(i, n, sum + nums[i], nums)
			if res > max:
				max = res
	dp[idx] = nums[idx] + max
	return dp[idx]

for i in range(n - 1, -1, -1):
	recur(i, n, 0, nums)
print(max(dp.values()))