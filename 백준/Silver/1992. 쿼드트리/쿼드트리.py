from sys import stdin
input = lambda : stdin.readline().rstrip()

def check(x_start, y_start, n, board) -> str:
    to_check = board[y_start][x_start]
    for i in range(y_start, y_start + n):
        for j in range(x_start, x_start + n):
            if board[i][j] != to_check:
                return '-1'
    return to_check


def recur(curr, n, board):
    global answer
    if n == 1:
        print(board[curr[0]][curr[1]], end='')
        return
    res = check(curr[1], curr[0], n, board)
    if res == '-1':
        print('(', end='')
        for i in range(curr[0], curr[0] + n, n // 2):
            for j in range(curr[1], curr[1] + n, n // 2):
                res = check(j, i, n // 2, board)
                if res == '-1':
                    recur((i, j), n // 2, board)
                else:
                    print(res, end='')
        print(')', end='')
    else:
        print(res, end='')



if __name__ == '__main__':
    n = int(input())
    board = []
    for _ in range(n):
        board.append(list(input()))
    recur((0, 0), n, board)