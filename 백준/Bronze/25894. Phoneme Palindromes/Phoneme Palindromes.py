from sys import stdin
input = stdin.readline

n = int(input())
test_case = 1
for _ in range(n):
	sound_n = int(input())
	sound_set = dict()
	for __ in range(sound_n):
		sound1, sound2 = input().strip().split()
		sound_set[sound1] = sound2
		sound_set[sound2] = sound1
	t = int(input())
	print(f'Test case #{test_case}:')
	test_case += 1
	for __ in range(t):
		word = input().strip()
		flag = False
		for i, j in zip(word, list(reversed(word))):
			if i != j:
				if i not in sound_set.keys() or j not in sound_set.keys():
					print(f'{word} NO')
					flag = True
				else:
					if sound_set[i] != j and sound_set[j] != i:
						print(f'{word} NO')
						flag = True
				break
		if not flag:
			print(f'{word} YES')
	if _ != n - 1:
		print()