from sys import stdin, stdout
input = stdin.readline
print = stdout.write


def check(n: int)->bool:
	if n == 1:
		return False
	i = 2
	while i < int(n**(1/2)):
		if not n % i:
			return False
		i += 1
	return True

m, n = map(int, input().split())
nums = [i for i in range(0, n + 1)]
end = int(n**(1/2))
for i in range(2, end + 1):
	if nums[i]:
		for j in range(i*i, n + 1, i):
			nums[j] = 0
nums[1] = 0
for i in range(m, n + 1):
	if nums[i]:
		print(f'{i}\n')