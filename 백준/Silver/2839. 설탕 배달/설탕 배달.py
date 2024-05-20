n = int(input())

kg = 0
count = 0
while kg < n:
	kg += 5
	count += 1
if kg == n:
	print(count)
else:
	kg -= 5
	count -= 1
	while (n - kg) % 3 and kg >= 0:
		kg -= 5
		count -= 1
	if kg > 0:
		print(count + (n - kg) // 3)
	else:
		if n % 3:
			print(-1)
		else:
			print(n // 3)