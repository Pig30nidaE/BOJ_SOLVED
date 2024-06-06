num = int(input())
count = 0
while num != 1:
	if num % 2: num += 1
	else: num //= 2
	count += 1
print(count)