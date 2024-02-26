from itertools import combinations
import sys
print = sys.stdout.write

n, m = map(int, input().split())

for i in combinations(range(1, n + 1), m):
	for j in i:
		print(str(j) + ' ')
	print('\n')