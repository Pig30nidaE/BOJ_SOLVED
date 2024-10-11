from sys import stdin
from collections import deque
input = lambda : stdin.readline().strip()


def main():
    t = int(input())
    for _ in range(t):
        p = input()
        n = int(input())
        arr = deque(eval(input()))

        try:
            reverseFlag = False
            for cmd in p:
                    if cmd == 'R':
                        reverseFlag = not reverseFlag
                    else:
                        if reverseFlag:
                            arr.pop()
                        else:
                            arr.popleft()
            print('[', end='')
            if not arr:
                print(']')
            else:
                if reverseFlag:
                    Range = range(len(arr) - 1, 0, -1)
                    last = 0
                else:
                    Range = range(len(arr) - 1)
                    last = -1
                for i in Range:
                    print(arr[i], end=',')
                print(f'{arr[last]}]')
        except IndexError:
            print('error')


if __name__ == '__main__':
    main()