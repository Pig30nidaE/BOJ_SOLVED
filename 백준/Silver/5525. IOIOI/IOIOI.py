from sys import stdin
input = lambda: stdin.readline()

n = int(input())
m = int(input())
s = input().strip()
tofind = 'I' + 'OI' * n
tofind_len = len(tofind)
count = 0
for i in range(m):
    if s[i] == 'I':
        j = 0
        while j < tofind_len and i + j < m and s[i + j] == tofind[j]:
            j += 1
        if j == tofind_len:
            count += 1
        else:
            i += j
print(count)
