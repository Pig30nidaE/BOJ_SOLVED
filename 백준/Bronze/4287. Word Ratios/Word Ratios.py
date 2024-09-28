from sys import stdin
from string import ascii_lowercase
input = stdin.readline

alpha = dict()
idx = 0
for i in ascii_lowercase:
	alpha[i] = idx
	idx += 1
words = list(input().strip().split())
while words[0] != '#':
	word1 = words[0]
	word2 = words[1]
	ans = ''
	for i in range(len(word1)):
		rotate = alpha[word2[i]] - alpha[word1[i]]
		last_idx = alpha[words[-1][i]]
		last_idx += rotate
		if last_idx >= len(ascii_lowercase):
			last_idx -= len(ascii_lowercase)
		ans += ascii_lowercase[last_idx]
	for i in words:
		print(i, end=' ')
	print(ans)
	words = list(input().strip().split())
	
