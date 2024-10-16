from sys import stdin
from collections import deque
input = lambda : stdin.readline()


def main():
    t = int(input())
    moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (-1, 2), (-1, -2), (1, 2), (1, -2)]
    for _ in range(t):
        l = int(input())
        curr = tuple(map(int, input().split()))
        target = tuple(map(int, input().split()))
        
        queue = deque()
        visited = set()
        queue.append((curr, 0))
        visited.add(curr)
        while queue:
            node = queue.popleft()
            if node[0] == target:
                print(node[1])
                break
            for i in moves:
                new_x, new_y = node[0][0] + i[0], node[0][1] + i[1]
                if 0 <= new_x < l and 0 <= new_y < l:
                    if (new_x, new_y) not in visited:
                        queue.append(((new_x, new_y), node[1] + 1))
                        visited.add((new_x, new_y))

if __name__ == '__main__':
    main()
