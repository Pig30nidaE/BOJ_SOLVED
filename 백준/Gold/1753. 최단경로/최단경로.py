from sys import stdin, stdout
import heapq
input = stdin.readline
print = stdout.write


def dijkstra(start, v, graph):
	INF = float('inf')
	dist = [INF] * (v + 1)
	dist[start] = 0
	heap = [(0, start)]
	while heap:
		weight, node = heapq.heappop(heap)
		if weight > dist[node]:
			continue
		for i, w in graph[node]:
			cost = weight + w
			if cost < dist[i]:
				dist[i] = cost
				heapq.heappush(heap, (cost, i))
	
	for i in range(1, v + 1):
		if dist[i] == INF:
			print('INF\n')
		else:
			print(f"{dist[i]}\n")

def solve():
	v, e = map(int, input().split())
	graph = [[] for _ in range(v + 1)]
	start = int(input())
	for _ in range(e):
		u, v_, w = map(int, input().split())
		graph[u].append((v_, w))
	dijkstra(start, v, graph)

if __name__ == '__main__':
	solve()