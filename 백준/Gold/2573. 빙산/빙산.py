from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 9)
input = lambda: stdin.readline()

def melt(iceberg: list, n: int, m: int) -> bool:
    to_melt = []
    for i in range(n):
        for j in range(m):
            if iceberg[i][j] > 0:
                water_count = 0
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    new_x, new_y = j + dx, i + dy
                    if 0 <= new_x < m and 0 <= new_y < n and iceberg[new_y][new_x] == 0:
                        water_count += 1
                if water_count > 0:
                    to_melt.append((i, j, water_count))
    
    if not to_melt:
        return True
    
    for i, j, water_count in to_melt:
        iceberg[i][j] = max(0, iceberg[i][j] - water_count)
    
    return False

def dfs(iceberg: list, n: int, m: int) -> int:
    visited = [[False] * m for _ in range(n)]
    count = 0
    
    def recur(y: int, x: int):
        stack = [(y, x)]
        visited[y][x] = True
        
        while stack:
            cy, cx = stack.pop()
            for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ny, nx = cy + dy, cx + dx
                if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and iceberg[ny][nx] > 0:
                    visited[ny][nx] = True
                    stack.append((ny, nx))

    for i in range(n):
        for j in range(m):
            if iceberg[i][j] > 0 and not visited[i][j]:
                recur(i, j)
                count += 1
    
    return count

n, m = map(int, input().split())
iceberg = [list(map(int, input().split())) for _ in range(n)]

year = 0
while True:
    count = dfs(iceberg, n, m)
    if count >= 2:
        print(year)
        break
    if melt(iceberg, n, m):
        print(0)
        break
    year += 1
