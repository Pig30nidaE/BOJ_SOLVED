from sys import stdin
input = stdin.readline

n = int(input())
battery = list(map(int, input().split()))
curr = 100
phone = -1
last = -1
for i in battery:
	if i == phone and last > 0:
		cost = last * 2
	else:
		cost = 2
	curr -= cost
	last = cost
	phone = i
	if curr <= 0:
		curr = 100
		last = -1
print(100 - curr)