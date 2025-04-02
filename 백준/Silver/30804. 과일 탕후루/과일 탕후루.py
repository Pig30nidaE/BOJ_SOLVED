from sys import stdin
input = lambda : stdin.readline()

n = int(input())
l = list(map(int, input().split()))
d = dict()
start = end = ans = 0
count = 0
while end < n:
    if l[end] not in d.keys():
        d[l[end]] = 1
        count += 1
        while count > 2:
            d[l[start]] -= 1
            if not d[l[start]]:
                del d[l[start]]
                count -= 1
            start += 1
    else:
        d[l[end]] += 1
    ans = max(ans, end - start + 1)
    end += 1
print(ans)