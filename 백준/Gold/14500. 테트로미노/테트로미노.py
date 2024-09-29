from sys import stdin
input = stdin.readline


def getMax(tetrominos_x: list, tetrominos_y: list, board: list, nm: tuple) -> int:
    max_ = 0
    n = nm[0]
    m = nm[1]

    for i in range(n):
        for j in range(m):
            for tx, ty in zip(tetrominos_x, tetrominos_y):
                sum_ = board[i][j]
                for x, y in zip(tx, ty):
                    new_y = i + y
                    new_x = j + x
                    if 0 <= new_y < n and 0 <= new_x < m:
                        sum_ += board[i + y][j + x]
                    else:
                        continue
                if sum_ > max_:
                    max_ = sum_
    return max_

def main():
    n, m = map(int, input().split())
    board = list()
    for _ in range(n):
        board.append(list(map(int, input().split())))
    tetrominos_x = [
        [1, 2, 3],
        [0, 0, 0], #
        [1, 0, 1], #
        [0, 0, 1],
        [-1, -2, -2],
        [0, 0, -1],
        [1, 2, 2], #
        [0, 0, -1],
        [-1, -2, -2],
        [0, 0, 1],
        [1, 2, 2],#
        [0, 1, 1],
        [-1, -1, -2],#
        [0, -1, -1],
        [-1, -1, -2],#
        [-1, 0, 1],
        [0, -1, 0],
        [-1, 0, 1],
        [0, 1, 0]
    ]
    tetrominos_y = [
        [0, 0, 0],
        [1, 2, 3], #
        [0, 1, 1], #
        [1, 2, 2],
        [0, 0, 1],
        [-1, -2, -2],
        [0, 0, -1],#
        [1, 2, 2],
        [0, 0, -1],
        [-1, -2, -2],
        [0, 0, 1], #
        [1, 1, 2],
        [0, 1, 1], #
        [1, 1, 2], 
        [0, -1, -1], #
        [0, -1, 0],
        [-1, 0, 1],
        [0, 1, 0],
        [-1, 0, 1]
    ]
    print(getMax(tetrominos_x, tetrominos_y, board, (n, m)))


if __name__ == '__main__':
    main()