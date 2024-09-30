from sys import stdin
input = lambda : stdin.readline().strip()

t = int(input())
p = list()
p.append(0)
p.append(1)
p.append(1)
last = 2
for _ in range(t):
	n = int(input())
	if n > last:
		for i in range(2, n + 1):
			p.append(p[last - 1] + p[last - 2])
			last += 1
	print(p[n])