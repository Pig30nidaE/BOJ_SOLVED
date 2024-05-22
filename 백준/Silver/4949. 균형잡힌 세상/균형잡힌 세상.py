from sys import stdin
input = stdin.readline

string = input()
stack = list()
while string != '.\n':
	stack.clear()
	flag = False
	for i in string:
		if i == '[':
			stack.append(i)
		elif i == '(':
			stack.append(i)
		elif i == ')':
			try:
				if stack[-1] == '(':
					stack.pop()
				else:
					print("no")
					flag = True
					break
			except IndexError:
				print("no")
				flag = True
				break
		elif i == ']':
			try:
				if stack[-1] == '[':
					stack.pop()
				else:
					print("no")
					flag = True
					break
			except IndexError:
				print("no")
				flag = True
				break
	if not flag:
		if stack:
			print("no")
		else:
			print("yes")
	string = input()
