from sys import stdin
input = lambda : stdin.readline()

count = dict()
count[0] = 0
count[-1] = 0
count[1] = 0

def check(n, paper, curr, tocheck):
    for i in range(n):
        for j in range(n):
            new_y, new_x = curr[0] + i, curr[1] + j
            if paper[new_y][new_x] != tocheck:
                return False
    return True


def recur(n, paper, curr) -> None:
    global count
    for i in range(0, n, n // 3):
        for j in range(0, n, n // 3):
            new_y, new_x = curr[0] + i, curr[1] + j
            if check(n // 3, paper, (new_y, new_x), paper[new_y][new_x]):
                count[paper[new_y][new_x]] += 1
            else:
                recur(n // 3, paper, (new_y, new_x))

if __name__ == '__main__':
    n = int(input())
    paper = []
    for _ in range(n):
        paper.append(list(map(int, input().split())))
    if check(n, paper, (0, 0), paper[0][0]):
        count[paper[0][0]] += 1
    else:
        recur(n, paper, (0, 0))
    print(count[-1])
    print(count[0])
    print(count[1])
    
