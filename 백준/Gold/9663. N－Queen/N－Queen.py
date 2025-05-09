n = int(input())
cnt = 0
cols = [False for _ in range(n)]
diag1 = [False for _ in range(2 * n)]
diag2 = [False for _ in range(2 * n)]


def recur(row, n):
    global cnt
    if row == n:
        cnt += 1
        return
    for col in range(n):
        new_diag1 = col + row
        new_diag2 = col - row
        if cols[col] or diag1[new_diag1] or diag2[new_diag2]:
            continue
        cols[col] = diag1[new_diag1] = diag2[new_diag2] = True
        recur(row + 1, n)
        cols[col] = diag1[new_diag1] = diag2[new_diag2] = False

recur(0, n)
print(cnt)
