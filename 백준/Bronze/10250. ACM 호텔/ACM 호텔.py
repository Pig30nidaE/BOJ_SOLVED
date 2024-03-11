import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
	h, w, n = map(int, input().split())
	room = 0
	flag = False
	for i in range(1, w + 1):
		for j in range(1, h + 1):
			room += 1
			if room == n:
				if i < 10:
					print(f'{j}0{i}')
				else:
					print(f'{j}{i}')
				flag = True
				break
		if flag:
			break