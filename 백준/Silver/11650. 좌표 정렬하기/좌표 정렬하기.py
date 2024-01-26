import sys
input = sys.stdin.readline

n = int(input())
coor = list()
for i in range(n):
	coor.append(tuple(map(int, input().split())))
for i in sorted(coor, key=lambda x:(x[0], x[1])):
	print(f'{i[0]} {i[1]}')