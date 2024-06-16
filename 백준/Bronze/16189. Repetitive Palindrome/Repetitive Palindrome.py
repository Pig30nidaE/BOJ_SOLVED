from sys import stdin
input = stdin.readline

s = input().strip()
k = int(input())

if list(s) == list(reversed(s)):
	print("YES")
else:
	print("NO")