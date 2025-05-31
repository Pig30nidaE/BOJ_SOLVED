from collections import deque


def solve():
    n, k = map(int, input().split())
    if n >= k:
        print(n - k)
        return
    last = 100001
    loc = [-1 for _ in range(last)]
    queue = deque()
    queue.append((n, 0))
    ans = float("inf")
    while queue:
        node = queue.popleft()
        if node[0] == k:
            if node[1] < ans:
                ans = node[1]
            continue
        walk_forward, walk_backward, teleport = node[0] + 1, node[0] - 1, node[0] * 2
        flag1 = flag2 = flag3 = False
        if 0 <= teleport < last:
            if loc[teleport] < 0 or node[1] < loc[teleport]:
                queue.append((teleport, node[1]))
                flag3 = True
        if 0 <= walk_forward < last:
            if loc[walk_forward] < 0 or node[1] + 1 < loc[walk_forward]:
                queue.append((walk_forward, node[1] + 1))
                flag1 = True
        if 0 <= walk_backward < last:
            if loc[walk_backward] < 0 or node[1] + 1 < loc[walk_backward]:
                queue.append((walk_backward, node[1] + 1))
                flag2 = True
        if flag1:
            loc[walk_forward] = node[1] + 1
        if flag2:
            loc[walk_backward] = node[1] + 1
        if flag3:
            loc[teleport] = node[1]
    print(ans)

if __name__ == '__main__':
    solve()