from sys import stdin, stdout
input = stdin.readline
print = stdout.write


def bellman_ford(start, graph, V):
    distance = [float('inf')] * V
    distance[start] = 0

    for _ in range(V - 1):
        for u, v, cost in graph:
            if distance[u] != float('inf') and distance[u] + cost < distance[v]:
                distance[v] = distance[u] + cost

    # 음수 사이클 체크
    for u, v, cost in graph:
        if distance[u] != float('inf') and distance[u] + cost < distance[v]:
            return "YES\n"

    return "NO\n"

def solve():
    tc = int(input())
    for _ in range(tc):
        n, m, w = map(int, input().split())
        road = []
        for __ in range(m):
            s, e, t = map(int, input().split())
            road.append((s, e, t))
            road.append((e, s, t))
        for __ in range(w):
            s, e, t = map(int, input().split())
            road.append((s, e, -t))
        for i in range(n + 1):
            road.append((n + 1, i, 0))
        
        print(bellman_ford(n + 1, road, n + 2))
if __name__ == '__main__':
    solve()