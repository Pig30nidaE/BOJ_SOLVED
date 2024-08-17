from sys import stdin
input = stdin.readline

n = int(input())
name = set()
for _ in range(n):
	name.add(input().strip())
if 'anj' in name: print("뭐야;")
else: print("뭐야?")