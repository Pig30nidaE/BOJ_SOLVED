from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))
start = 0
end = max(trees)
while start <= end:
	middle = start + (end - start) // 2
	get_tree = sum(map(lambda x:x - middle if x >= middle else 0, trees))
	if get_tree >= m: start = middle + 1
	else: end = middle - 1
print(end)