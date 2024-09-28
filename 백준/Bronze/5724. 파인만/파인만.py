from sys import stdin
input = stdin.readline


n = int(input())
while n:
	print(sum(i ** 2 for i in range(1, n + 1)))
	n = int(input())