from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    tower = list(map(int, input().split()))
    stack = []
    idx = 0
    value = 1
    for i in range(n):
        if stack:
            if tower[i] < stack[-1][value]:
                print(stack[-1][idx], end=' ')
            else:
                while stack and stack[-1][value] < tower[i]:
                    stack.pop()
                if stack:
                    print(stack[-1][idx], end=' ')
                else:
                    print(0, end=' ')
        else:
            print(0, end=' ')
        stack.append((i + 1, tower[i]))

if __name__ == '__main__':
    main()