from sys import stdin
input = stdin.readline

n = int(input())

for t in range(1, n + 1):
	list1 = list(input().strip())
	list2 = list(input().strip())
	tmp = list2.copy()
	for i in list1:
		try: list2.remove(i)
		except ValueError: pass
	for i in tmp:
		try: list1.remove(i)
		except ValueError: pass
	print(f'Case #{t}: {len(list1) + len(list2)}')