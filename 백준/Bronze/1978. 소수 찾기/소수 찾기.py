import math


def isPrime(num: int)->bool:
	for i in range(2, int(math.sqrt(num) + 1)):
		if not num % i:
			return False
	return True

n = int(input())
nums = list(map(int, input().split()))
count = 0
for i in nums:
	if i == 1:
		continue
	if isPrime(i):
		count += 1
print(count)