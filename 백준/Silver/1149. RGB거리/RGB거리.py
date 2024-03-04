import sys
input = sys.stdin.readline


n = int(input())
memo = list()
memo.append(list(map(int, input().split())))

for i in range(1, n):
	memo.append(list(map(int, input().split())))
	memo[i][0] += memo[i - 1][1] if memo[i - 1][1] < memo[i - 1][2] else memo[i - 1][2]
	memo[i][1] += memo[i - 1][0] if memo[i - 1][0] < memo[i - 1][2] else memo[i - 1][2]
	memo[i][2] += memo[i - 1][1] if memo[i - 1][1] < memo[i - 1][0] else memo[i - 1][0]
print(min(memo[n - 1]))