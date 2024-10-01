from sys import stdin
from collections import deque

input = lambda: stdin.readline().strip()

# DSLR 연산 정의
def operation_d(n: int) -> int:
    return (n * 2) % 10000

def operation_s(n: int) -> int:
    return (n - 1) % 10000

def operation_l(n: int) -> int:
    return (n % 1000) * 10 + n // 1000

def operation_r(n: int) -> int:
    return (n % 10) * 1000 + n // 10

def main():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())

        parent = [-1] * 10000
        operations = [''] * 10000

        queue = deque([a])
        visited = [False] * 10000
        visited[a] = True

        while queue:
            curr = queue.popleft()

            if curr == b:
                break

            for op, func in zip('DSLR', [operation_d, operation_s, operation_l, operation_r]):
                next_val = func(curr)

                if not visited[next_val]:
                    visited[next_val] = True
                    parent[next_val] = curr
                    operations[next_val] = op
                    queue.append(next_val)
        path = []
        while b != a:
            path.append(operations[b])
            b = parent[b]

        print(''.join(reversed(path)))

if __name__ == '__main__':
    main()
