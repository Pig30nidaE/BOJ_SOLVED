n = int(input())
for i in range(n):
	to_str = str(i)
	k = sum([int(j) for j in to_str])
	if k + i == n:
		print(i)
		exit()
print(0)