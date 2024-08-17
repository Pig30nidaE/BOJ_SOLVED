from sys import stdin
input = stdin.readline

while True:
	route, size = input().strip().split()
	if route == "#":
		break
	size = int(size)

	passengers = int(input())
	testcase = int(input())

	for _ in range(testcase):
		out_, in_ = map(int, input().split())
		passengers -= out_
		passengers = max(0, passengers) 
		passengers += min(in_, size - passengers)
	
	print(f"{route} {passengers}")