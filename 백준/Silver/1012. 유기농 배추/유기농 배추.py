from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 9)
input = lambda : stdin.readline()

visited = set()
def recur(x, y, farm, info) -> None:
    global visited
    visited.add((x, y))
    for i, j in zip([-1, 0, 1, 0], [0, -1, 0, 1]):
        new_x, new_y = x + i, y + j
        if 0 <= new_x < info[0] and 0 <= new_y < info[1]:
            if (new_x, new_y) not in visited and farm[new_y][new_x]:
                recur(new_x, new_y, farm, info)

def dfs(m, n, farm) -> int:
    global visited
    visited = set()
    count = 0
    for y in range(n):
        for x in range(m):
            if (x, y) not in visited and farm[y][x]:
                count += 1
                recur(x, y, farm, (m, n))
    return count

def solution() -> None:
    t = int(input())
    for _ in range(t):
        m, n, k = map(int, input().split())
        farm = [[0 for col in range(m)] for row in range(n)]
        for __ in range(k):
            x, y = map(int, input().split())
            farm[y][x] = 1
        print(dfs(m, n, farm))
if __name__ == '__main__':
    solution()
