from sys import stdin
input = lambda : stdin.readline().strip()


def solve():
	str1 = input()
	str2 = input()
	len1 = len(str1)
	len2 = len(str2)
	dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

	for idx1 in range(1, len1 + 1):
		for idx2 in range(1, len2 + 1):
			if str1[idx1 - 1] == str2[idx2 - 1]:
				dp[idx1][idx2] = dp[idx1 - 1][idx2 - 1] + 1
			else:
				dp[idx1][idx2] = max(dp[idx1 - 1][idx2], dp[idx1][idx2 - 1])
	print(dp[len1][len2])


if __name__ == '__main__':
	solve()