from sys import stdin
input = lambda : stdin.readline()


a = int(input())
b = int(input())
c = int(input())

for i in range(10):
    print(f'{str(a * b * c).count(str(i))}')