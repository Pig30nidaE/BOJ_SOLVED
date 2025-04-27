from sys import stdin, stdout
input = stdin.readline
print = stdout.write



def main():
	n = int(input())
	string_len = int(input())
	string = input().strip()
	IOI = 'IOI'
	
	i = loop = count = 0
	while i <= string_len - 3:
		if string[i:i + 3] == IOI:
			i += 2
			loop += 1
			if loop == n:
				count += 1
				loop -= 1
		else:
			loop = 0
			i += 1
	print(f'{count}')

if __name__ == '__main__':
	main()
