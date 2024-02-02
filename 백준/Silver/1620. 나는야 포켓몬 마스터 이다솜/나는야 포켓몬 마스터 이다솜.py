import sys

input = sys.stdin.readline

n, m = map(int, input().split())
for_num = dict()
for_name = dict()
for i in range(1, n + 1):
	name = input().strip()
	for_num[i] = name
	for_name[name] = i
for i in range(m):
	tofind = input().strip()
	if tofind.isdecimal():
		print(for_num[int(tofind)])
	else:
		print(for_name[tofind])
