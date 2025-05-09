def check(row, col, cols, diags1, diags2) -> bool:
    if col in cols or row + col in diags1 or row - col in diags2:
        return False
    return True

def recur(depth, n, cols, diags1, diags2, count) -> int:
    if depth == n:
        return 1
    for i in range(n):
        if check(depth, i, cols, diags1, diags2):
            cols.add(i)
            diags1.add(depth + i)
            diags2.add(depth - i)
            count += recur(depth + 1, n, cols, diags1, diags2, 0)
            cols.remove(i)
            diags1.remove(depth + i)
            diags2.remove(depth - i)
    return count

def solution():
    n = int(input())
    print(recur(0, n, set(), set(), set(), 0))

if __name__ == '__main__':
    solution()