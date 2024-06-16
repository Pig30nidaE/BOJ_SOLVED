from itertools import combinations
from sys import stdin
input = stdin.readline

n = int(input())
name = list()
for _ in range(n):
	name.append(input().strip())

count = 0
for i in list(combinations(name, 2)):
	flag = False
	for j in range(len(i[0]) - 1, -1, -1):
		try:
			if i[0][j] == i[1][0]:
				cut = i[0][j:]
				cut_flag = False
				for k in range(len(cut)):
					if cut[k] != i[1][k]:
						cut_flag = True
						break
				if not cut_flag:
					flag = True
					count += 1
					break
		except IndexError:
			break
	if not flag:
		for j in range(len(i[1]) - 1, -1, -1):
			try:
				if i[1][j] == i[0][0]:
					cut = i[1][j:]
					cut_flag = False
					for k in range(len(cut)):
						if cut[k] != i[0][k]:
							cut_flag = True
							break
					if not cut_flag:
						flag = True
						count += 1
						break
			except IndexError:
				break
print(count)