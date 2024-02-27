from itertools import permutations
import sys
input = sys.stdin.readline
print = sys.stdout.write

n, m = map(int, input().split())
nums = list(map(int, input().split()))

for i in sorted(list(set(permutations(nums, m)))):
	for j in i:
		print(f'{j} ')
	print('\n')