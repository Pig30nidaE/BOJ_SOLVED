from itertools import product
import sys
input = sys.stdin.readline


t = int(input())
nums = [1, 2, 3]
for i in range(t):
	count = 0
	n = int(input())
	for j in range(n):
		comb = product(nums, repeat=j+1)
		for k in comb:
			if sum(k) == n:
				count += 1
	print(count)
