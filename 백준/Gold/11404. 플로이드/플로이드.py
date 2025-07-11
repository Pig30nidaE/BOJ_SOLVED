from sys import stdin
input = stdin.readline


def solve():
    n = int(input())
    m = int(input())
    INF = float('INF')
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        if graph[a][b] < INF:
            if c < graph[a][b]:
                graph[a][b] = c
        else:
            graph[a][b] = c
    for i in range(n + 1):
        graph[i][i] = 0
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][j] == INF:
                print(0, end=' ')
            else:
                print(graph[i][j], end=' ')
        print()

if __name__ == '__main__':
    solve()