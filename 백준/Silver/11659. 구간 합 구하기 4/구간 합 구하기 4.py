import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
memo = list()
memo.append(0)
sums = 0
for i in range(n):
	sums += nums[i]
	memo.append(sums)
for _ in range(m):
	start, end = map(int, input().split())
	print(memo[end] - memo[start - 1])
