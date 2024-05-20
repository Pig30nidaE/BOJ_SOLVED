from sys import stdin
input = stdin.readline


n = int(input())
l = [0 for i in range(n)]
for i in range(n):
	l[i] = tuple(map(int, input().split()))
for i in l:
	rank = 1
	for j in l:
		if i[0] < j[0] and i[1] < j[1]:
			rank += 1
	print(rank, end=" ")