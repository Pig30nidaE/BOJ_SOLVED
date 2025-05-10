from sys import stdin, stdout
from itertools import combinations_with_replacement
input = stdin.readline
print = stdout.write


n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

for i in sorted(list(set(combinations_with_replacement(nums, m)))):
	for elm in i:
		print(f'{elm} ')
	print('\n')