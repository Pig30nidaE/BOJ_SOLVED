formula = input()
stack = list()
for i in formula:
	if i.isdigit(): stack.append(int(i))
	else:
		res1 = stack.pop()
		res2 = stack.pop()
		stack.append(int(eval(f'{res2} {i} {res1}')))
print(stack.pop())