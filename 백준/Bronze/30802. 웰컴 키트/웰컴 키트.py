from sys import stdin
input = stdin.readline

n = int(input())
people = list(map(int, input().split()))
t, p = map(int, input().split())
print(sum(((i - 1) // t) + 1 for i in people))
print(f'{n // p} {n - p * (n//p)}')