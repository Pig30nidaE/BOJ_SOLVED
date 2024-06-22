n = int(input())
if n == 1: print(1)
elif n == 2: print(3)
else:
	i = 1
	divisor = list()
	while i * i < n:
		if not n % i:
			divisor.append(i)
			divisor.append(n // i)
		i += 1
	print(sum(divisor))