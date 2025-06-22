from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(10 ** 6)

def dfs(curr: int, graph: dict, memo: dict) -> int:
    if curr in memo:
        return memo[curr]
    if curr not in graph:
        memo[curr] = 0
        return 0

    max_dist = 0
    for child, weight in graph[curr]:
        dist = dfs(child, graph, memo) + weight
        if dist > max_dist:
            max_dist = dist
    memo[curr] = max_dist
    return max_dist

def solution():
    n = int(input())
    graph = dict()

    for _ in range(n - 1):
        p, c, w = map(int, input().split())
        if p not in graph:
            graph[p] = []
        graph[p].append((c, w))

    answer = 0
    memo = {}

    for key in graph.keys():
        distances = [dfs(child, graph, memo) + weight for child, weight in graph[key]]
        distances.sort(reverse=True)

        if len(distances) >= 2:
            radius = distances[0] + distances[1]
        else:
            radius = distances[0]

        if radius > answer:
            answer = radius

    print(answer)

if __name__ == '__main__':
    solution()
