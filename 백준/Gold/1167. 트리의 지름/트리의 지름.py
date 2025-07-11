from sys import stdin
from collections import deque
input = stdin.readline


def bfs(start, graph):
    queue = deque()
    queue.append((start, 0))
    visited = {start}
    dist = 0
    point = 0
    while queue:
        node = queue.popleft()
        if node[0] in graph:
            flag = False
            for next in graph[node[0]]:
                if next[0] not in visited:
                    queue.append((next[0], next[1] + node[1]))
                    visited.add(next[0])
                    flag = True
            if not flag:
                if node[1] > dist:
                    dist = node[1]
                    point = node[0]
    return point, dist

def solve():
    v = int(input())
    graph = dict()
    for _ in range(v):
        info = list(map(int, input().split()))
        if info[0] not in graph:
            graph[info[0]] = []
        for i in range(1, len(info) - 1, 2):
            graph[info[0]].append((info[i], info[i + 1]))

    start, dist = bfs(1, graph)
    end, ans = bfs(start, graph)
    print(ans)

if __name__ == '__main__':
    solve()