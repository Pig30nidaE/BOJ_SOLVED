from sys import stdin, stdout
input = stdin.readline
print = stdout.write

n = int(input())
cor = list()
for i in range(n): #10만
	cor.append(tuple(map(int, input().split())))
cor.sort(key=lambda x:(x[1], x[0])) #50만
for i in cor:
	print(f'{i[0]} {i[1]}\n')