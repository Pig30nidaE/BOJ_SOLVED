from sys import stdin
from collections import deque
input = stdin.readline

n = int(input())
sequence = deque()
for _ in range(n):
	sequence.append(int(input()))

if n == 1:
	for i in range(1, sequence[0] + 1):
		print("+")
	print("-")
	exit()

stack = list()

start = 1
i = 1
ans = ""
while sequence:
	num = sequence.popleft()
	while i <= n + 1:
		if i <= num:
			stack.append(i)
			i += 1
			ans += "+\n"
		elif i > num:
			ans += "-\n"
			if stack: 
				stackTop = stack.pop()
			if stackTop != num:
				print("NO")
				exit()
			if sequence:
				num = sequence.popleft()
			else: 
				i += 1
print(ans)