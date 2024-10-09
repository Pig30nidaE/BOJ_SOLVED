from sys import stdin
input = stdin.readline


n = int(input())
seq = []
for _ in range(n):
    seq.append(int(input()))
stack = []
topop = 0
answer = []
try:
    for i in range(1, n + 1):
        stack.append(i)
        answer.append('+')
        while stack and stack[-1] == seq[topop]:
            stack.pop()
            answer.append('-')
            topop += 1
except IndexError:
    print("NO")
if stack:
    print("NO")
else:
    for i in answer:
        print(i)

    