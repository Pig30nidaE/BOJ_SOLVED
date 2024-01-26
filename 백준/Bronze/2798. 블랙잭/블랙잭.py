from itertools import combinations

n, m = map(int, input().split())
nums = list(map(int, input().split()))
combs = list(combinations(nums, 3))

to_print = 0

for i in combs:
	sums = sum(i)
	if sums <= m and sums > to_print:
		to_print = sums
print(to_print)
