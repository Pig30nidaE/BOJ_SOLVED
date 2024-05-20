n = int(input())
k = 0
idx = 1
count = 1
while idx < n:
	k += 6
	idx += k
	count += 1
print(count)