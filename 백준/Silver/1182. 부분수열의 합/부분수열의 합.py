from itertools import combinations
import sys

input = sys.stdin.readline
n, s = map(int, input().split())
sequence = list(map(int, input().strip().split()))

count = 0
for i in range(1, n + 1):
	for j in list(combinations(sequence, i)):
		if sum(j) == s:
			count += 1
print(count)