import sys
input = sys.stdin.readline
INF = float("inf")


n = int(input())
k = int(input())

dp = [[INF]*21 for _ in range(n+1)]
dp[0][1] = 0
for i in range(1, n+1):
    _, *holes = map(int, input().split())

    for hole in holes:
        o = dp[i-1][hole]
        a = dp[i-1][hole-1] if hole > 1 else INF
        c = dp[i-1][hole+1] if hole < 20 else INF

        b = INF
        if hole == 20:
            b = min(dp[i-1][10:])
        elif not hole % 2:
            b = dp[i-1][hole >> 1]

        now = min(a, b, c, o)

        dp[i][hole] = now if now != INF else (min(dp[i-1]) + 1)

ans = min(dp[n])
print(ans if ans <= k else -1)