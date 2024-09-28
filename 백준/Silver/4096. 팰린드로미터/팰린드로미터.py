from sys import stdin
input = stdin.readline

string = input().strip()
format_num = len(string)
while string != '0':
	count = 0
	while string != string[::-1]:
		string = str(format(int(string) + 1, '0' + str(format_num)))
		count += 1
	print(count)
	string = input().strip()
	format_num = len(string)