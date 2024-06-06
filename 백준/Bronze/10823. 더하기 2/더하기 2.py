from sys import stdin
input = stdin.readline

string = ""
num = 0
tmp = input().strip()
while tmp:
	for char in tmp:
		if char == ',':
			num += int(string)
			string = ""
		else:
			string += char
	tmp = input().strip()
print(int(string) + num)

