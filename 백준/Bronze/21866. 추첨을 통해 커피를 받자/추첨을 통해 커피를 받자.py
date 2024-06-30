scores = list(map(int, input().split()))
table = [100, 100, 200, 200, 300, 300, 400, 400, 500]
for i, j in zip(scores, table):
	if i > j:
		print("hacker")
		exit()
ans = sum(scores)
if ans >= 100:
	print("draw")
else:
	print("none")