from sys import stdin
input = lambda: stdin.readline()

n = int(input())
m = int(input())
s = input().strip()
tofind = 'I' + 'OI' * n
tofind_len = 1 + 2 * n
count = 0
for i in range(m - tofind_len + 1):
    if s[i] == 'I':
        j = 0
        while j < tofind_len and s[i + j] == tofind[j]:
            j += 1
        if j == tofind_len:
            count += 1
        i += j
print(count)
