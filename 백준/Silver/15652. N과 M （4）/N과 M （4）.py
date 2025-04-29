from sys import stdin, stdout
from itertools import combinations_with_replacement
input = stdin.readline
print = stdout.write


def solution():
    n, m = map(int, input().split())
    for i in list(combinations_with_replacement(range(1, n + 1), m)):
        for j in i:
            print(f'{j} ')
        print('\n')


if __name__ == '__main__':
    solution()