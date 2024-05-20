from math import factorial

n = str(factorial(int(input())))
count = 0
for i in list(reversed(n)):
	if i == '0':
		count += 1
	else:
		print(count)
		break