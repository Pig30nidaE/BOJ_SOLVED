from sys import setrecursionlimit
setrecursionlimit(1000000000)

a, b, c, = map(int, input().split())

def recur(a: int, b: int, c: int)->int:
	if b == 1:
		return a % c
	elif not b % 2:
		return (recur(a, b // 2, c) ** 2) % c
	else:
		return ((recur(a, b // 2, c) ** 2) * a) % c

print(recur(a, b, c))