from sys import stdin
input = lambda : stdin.readline().strip()


step = int(input())
user = 0

while step:
    n = int(input())
    user += 1
    print(f'User {user}')
    for _ in range(n):
        print(f'{int(input()) * step / 100000:.5f}')
    step = int(input())