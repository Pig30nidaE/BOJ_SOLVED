n = int(input())
for i in range(n):
	sum = 0
	ox = list(input())
	count = 0
	for j in range(len(ox)):
		if ox[j] == 'O':
			count += 1
			sum += count
		else: count = 0
	print(sum)

