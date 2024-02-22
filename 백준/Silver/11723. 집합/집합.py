import sys
input = sys.stdin.readline
n = int(input())

Set = set()
for i in range(n):
	command = list(input().split())
	if len(command) > 1:
		command[1] = int(command[1])
		if command[0][0] == 'a':
			Set.add(command[1])
		elif command[0][0] == 'r':
			if command[1] in Set:
				Set.remove(command[1])
		elif command[0][0] == 'c':
			if command[1] in Set: print(1)
			else: print(0)
		else:
			if command[1] in Set:
				Set.remove(command[1])
			else: Set.add(command[1])
	else:
		if command[0][0] == 'e':
			Set.clear()
		else:
			Set = set(i for i in range(1, 21))