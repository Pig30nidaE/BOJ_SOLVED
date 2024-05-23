from sys import stdin
import statistics
from collections import Counter
input = stdin.readline

n = int(input())
nums = list()
for _ in range(n):
	nums.append(int(input()))
sorted_nums = sorted(nums)

print(round(statistics.mean(nums)))
print(statistics.median(nums))
c = Counter(sorted_nums).most_common()
if n > 1:
	if c[0][1] == c[1][1]:
		print(c[1][0])
	else:
		print(c[0][0])
else:
	print(c[0][0])
print(sorted_nums[-1] - sorted_nums[0])
