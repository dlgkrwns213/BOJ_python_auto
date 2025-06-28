# https://www.acmicpc.net/problem/13910
INF = float('inf')

n, m = map(int, input().split())
woks = list(map(int, input().split()))

dp = [INF] * (n+1)
dp[0] = 0
for weight in range(1, n+1):
    for i, woki in enumerate(woks):
        if weight < woki:
            continue

        mn = dp[weight-woki] + 1
        for wokj in woks[:i]:
            if weight < wokj:
                continue

            mn = min(mn, dp[weight-wokj] + 1)
            if weight < woki + wokj:
                continue
            mn = min(mn, dp[weight-woki-wokj] + 1)

        dp[weight] = min(dp[weight], mn)

print(dp[n] if dp[n] != INF else -1)