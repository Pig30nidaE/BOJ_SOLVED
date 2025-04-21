from sys import stdin, stdout
from heapq import heappush, heappop
input = stdin.readline
print = stdout.write


def solution():
    n = int(input())
    plus_heap = []
    minus_heap = []
    for _ in range(n):
        op = int(input())
        if op > 0:
            heappush(plus_heap, op)
        elif op < 0:
            heappush(minus_heap, -op)
        else:
            if plus_heap and minus_heap:
                if plus_heap[0] >= minus_heap[0]:
                    print(f'{-heappop(minus_heap)}')
                else:
                    print(f'{heappop(plus_heap)}')
            elif plus_heap:
                print(f'{heappop(plus_heap)}')
            elif minus_heap:
                print(f'{-heappop(minus_heap)}')
            else:
                print('0')
            print('\n')


if __name__ == '__main__':
    solution()