n = input()
while n != '0':
	rev_idx = -1
	flag = 0
	for i in range(len(n)//2):
		if n[i]!= n[rev_idx]:
			print("no")
			flag = 1
			break
		rev_idx -= 1
	if not flag:
		print("yes")
	n = input()
