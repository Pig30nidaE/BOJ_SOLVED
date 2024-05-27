from sys import stdin
input = stdin.readline


k, n = map(int, input().split())
nums = list()
for _ in range(k):
	nums.append(int(input()))
nums.sort()

start = 1
end = nums[-1]

while start <= end:
	mid = (start + end) // 2
	count = 0
	for i in nums:
		count += i // mid
	if count >= n:
		start = mid + 1
	else:
		end = mid - 1
print(end)