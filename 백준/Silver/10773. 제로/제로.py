from sys import stdin
input = stdin.readline

k = int(input())
stack = list()
for _ in range(k):
	num = int(input())
	if num == 0: stack.pop()
	else: stack.append(num)
print(sum(stack))