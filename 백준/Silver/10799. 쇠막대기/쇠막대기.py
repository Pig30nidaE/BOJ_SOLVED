from sys import stdin
input = lambda : stdin.readline().strip()

bar = input().replace('()', '|')
count = 0
stack = []
for i in bar:
    if i == '|':
        count += len(stack)
    elif i == '(':
        stack.append(i)
    else:
        count += 1
        stack.pop()
print(count)