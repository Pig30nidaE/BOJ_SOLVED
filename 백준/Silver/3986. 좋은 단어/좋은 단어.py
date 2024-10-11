from sys import stdin
input = lambda : stdin.readline().strip()


n = int(input())
count = 0
for _ in range(n):
    stack = []
    string = input()
    idx = 0
    while idx < len(string):
        if stack and string[idx] == stack[-1]:
                stack.pop()
        else:
            stack.append(string[idx])
        idx += 1
    if not stack:
        count += 1
print(count)

            