from itertools import permutations


n, m = map(int, input().split())
nums = list(map(int, input().split()))

to_print = list()
for i in permutations(nums, m):
	to_print.append(i)
to_print.sort()
for i in to_print:
	for j in i:
		print(j, end=" ")
	print()