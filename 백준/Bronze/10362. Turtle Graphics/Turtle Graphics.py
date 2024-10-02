from sys import stdin
input = lambda : stdin.readline().strip()


t = int(input())
for case in range(1, t + 1):
    location = list(map(int, input().split()))
    board = list()
    for _ in range(64):
        board.append([0 for i in range(64)])
    board[location[1]][location[0]] = 1
    path = input()
    dir_idx = 0
    dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    n = 0
    for operation in path:
        if operation == 'F':
            location[0] += dir[dir_idx][0]
            location[1] += dir[dir_idx][1]
            if board[location[1]][location[0]] == 1:
                n += 1
            board[location[1]][location[0]] += 1
        elif operation == 'R':
            dir_idx = (dir_idx + 1) % 4
        else:
            dir_idx = (dir_idx - 1) % 4
    print(f'Case #{case}: {location[0]} {location[1]} {n}')
                
