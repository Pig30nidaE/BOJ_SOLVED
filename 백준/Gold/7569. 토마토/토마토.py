from sys import stdin
from collections import deque
input = lambda : stdin.readline()


def main():
    m, n, h = map(int, input().split())
    farm = list()
    for _ in range(h):
        tmp = list()
        for __ in range(n):
            tmp.append(list(map(int, input().split())))
        farm.append(tmp)

    queue = deque()
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if farm[i][j][k] == 1:
                    queue.append([(i, j, k), 0])
    while queue:
        node = queue.popleft()
        for i, j in zip([-1, 0, 1, 0], [0, -1, 0, 1]):
            new_x, new_y = j + node[0][2], i + node[0][1]
            if 0 <= new_x < m and 0 <= new_y < n:
                if not farm[node[0][0]][new_y][new_x]:
                    farm[node[0][0]][new_y][new_x] = 1
                    queue.append([(node[0][0], new_y, new_x), node[1] + 1])
        for k in [-1, 1]:
            new_z = node[0][0] + k
            if 0 <= new_z < h:
                if not farm[new_z][node[0][1]][node[0][2]]:
                    farm[new_z][node[0][1]][node[0][2]] = 1
                    queue.append([(new_z, node[0][1], node[0][2]), node[1] + 1])
        
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if not farm[i][j][k]:
                    print(-1)
                    return
    print(node[1])
                



if __name__ == '__main__':
    main()