from sys import stdin
input = stdin.readline


def main():
	t = int(input())
	for _ in range(t):
		clothes = dict()
		n = int(input())
		for __ in range(n):
			name, category = input().strip().split()
			try:
				clothes[category].append(name)
			except KeyError:
				clothes[category] = [name]
		ans = 1
		for value in clothes.values():
			ans *= len(value) + 1
		print(ans - 1)

if __name__ == '__main__':
	main()