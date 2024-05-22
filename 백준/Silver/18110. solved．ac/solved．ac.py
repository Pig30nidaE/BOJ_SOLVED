from sys import stdin
from statistics import mean
import math
input = stdin.readline

n = int(input())
if not n:
	print(0)
	exit()
scores = [0 for i in range(n)]
for i in range(n):
	scores[i] = int(input())
scores.sort()
cut = n * 0.15
if cut - cut // 1 >= 0.5: aver = math.ceil(cut)
else: aver = math.floor(cut)
scores = scores[aver:n - aver]
ans = mean(scores)
if ans - ans // 1 >= 0.5: ans = math.ceil(ans)
else: ans = math.floor(ans)
print(ans)
