import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
s = list()
for i in range(n):
	s.append(''.join(sorted(input().strip())))
s = sorted(list(s))

string = ""
for i in range(k):
	string += s[i]
print(''.join(sorted(list(string))))