n = int(input())
cnt = 0

def recur(row, cols, diag1, diag2):
    global cnt
    if row == n:
        cnt += 1
        return

    # 가능한 모든 자리: n비트 모두 켜기 -> ~(cols | diag1 | diag2)
    avail = (~(cols | diag1 | diag2)) & ((1 << n) - 1)
    while avail:
        pick = avail & -avail  # 가장 오른쪽 비트만 선택
        avail -= pick
        recur(row + 1,
              cols | pick,
              (diag1 | pick) << 1,
              (diag2 | pick) >> 1)

recur(0, 0, 0, 0)
print(cnt)
