from sys import stdin
from collections import deque

input = lambda : stdin.readline()

def solution():
    n = int(input())
    islands = []
    for i in range(n):
        islands.append(list(map(int, input().split())))

    visited = [[False for col in range(n)] for row in range(n)]

    flag = 0
    for i in range(n):
        for j in range(n):
            if islands[i][j] and not visited[i][j]:
                queue = deque()
                queue.append((j, i))
                flag += 1
                while queue:
                    node = queue.popleft()
                    islands[node[1]][node[0]] = flag
                    for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                        nx, ny = node[0] + dx, node[1] + dy
                        if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx] and islands[ny][nx]:
                            visited[ny][nx] = True
                            queue.append((nx, ny))

    min = n * n
    for i in range(n):
        for j in range(n):
            queue = deque()
            queue.append(((j, i), 0))
            color = islands[i][j]
            if color:
                visited = set()
                while queue:
                    node = queue.popleft()
                    if islands[node[0][1]][node[0][0]] and islands[node[0][1]][node[0][0]] != color:
                        if node[1] < min:
                            min = node[1]
                        break
                    for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                        nx, ny = node[0][0] + dx, node[0][1] + dy
                        if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited and islands[ny][nx] != color:
                            queue.append(((nx, ny), node[1] + 1))
                            visited.add((nx, ny))
    print(min - 1)


if __name__ == '__main__':
    solution()