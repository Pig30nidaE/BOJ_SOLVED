from sys import stdin
input = stdin.readline

n = int(input())
string = input().strip()
q = int(input())
for _ in range(q):
	l, r = map(int, input().split())
	new_string = string[l - 1: r]
	max_count = 0
	for i in range(len(new_string)):
		count = 0
		for j, k in zip(range(i + 1, len(new_string)), range(i, -1, -1)):
			if new_string[j] == new_string[k]:
				count += 1
		if count > max_count:
			max_count = count
	print(max_count)
