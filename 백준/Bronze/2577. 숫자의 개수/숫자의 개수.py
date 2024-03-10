a = int(input())
b = int(input())
c = int(input())
num = str(a*b*c)
temp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in num:
	temp[int(i)] += 1
for i in temp:
	print(i)
	