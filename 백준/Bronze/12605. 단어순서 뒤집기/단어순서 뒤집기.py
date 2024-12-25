from sys import stdin
input = lambda : stdin.readline().strip()


n = int(input())
for i in range(1, n + 1):
	words = list(reversed(input().split()))
	print(f'Case #{i}:', end=' ')
	for j in words: print(f'{j}', end=' ')
	print()