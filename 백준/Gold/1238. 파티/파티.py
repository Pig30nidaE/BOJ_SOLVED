from sys import stdin
import heapq
input = stdin.readline


def dijkstra(start, graph):
    INF = float('inf')
    n = len(graph)  # 정점 개수 (graph는 0부터 인덱스 시작)
    dist = [INF] * (n + 1)
    dist[start] = 0
    
    pq = []
    heapq.heappush(pq, (0, start))  # (거리, 정점)
    
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        
        # 이미 처리된 노드이면 무시
        if dist[current_node] < current_dist:
            continue
        
        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return dist
    


def solve():
    n, m, x = map(int, input().split())
    graph = dict()
    for _ in range(m):
        start, end, t = map(int, input().split())
        if start in graph: graph[start].append((end, t))
        else: graph[start] = [(end, t)]
    info = [[0] * (n + 1) for _ in range(n + 1)]
    for start in range(1, n + 1):
        dist = dijkstra(start, graph)
        for i in range(1, n + 1):
            info[start][i] = dist[i]

    ans = 0
    for i in range(1, n + 1):
        ans = max(ans, info[i][x] + info[x][i])
    print(ans)


if __name__ == '__main__':
    solve()