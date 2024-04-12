import sys
input = sys.stdin.readline

passwd = dict()
n, m = map(int, input().split())
for _ in range(n):
	site, pw = input().strip().split()
	passwd[site] = pw
for _ in range(m):
	print(passwd[input().strip()])