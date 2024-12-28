from sys import stdin
input = stdin.readline


if __name__ == '__main__':
    n = int(input())
    dp = [0, 1]
    for i in range(2, n + 1):
        min_ = 4
        j = 1
        while i - j * j >= 0:
            min_ = min(min_, dp[i - j * j])
            j += 1
        dp.append(min_ + 1)
    print(dp[n])
