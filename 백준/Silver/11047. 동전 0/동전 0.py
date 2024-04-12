import sys
input = sys.stdin.readline
n, k = map(int, input().split())

coins = list()
idx = -1
for i in range(n):
	coins.append(int(input()))
	if coins[-1] > k:
		break
count = 0
while k:
	if k - coins[-1] >= 0:
		tmp = k // coins[-1]
		k -= tmp * coins[-1]
		count += tmp
	else:
		coins.pop()
print(count)
