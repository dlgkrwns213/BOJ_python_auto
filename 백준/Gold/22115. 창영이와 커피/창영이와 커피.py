# https://www.acmicpc.net/problem/22115
INF = int(1e9)

n, k = map(int, input().split())
caffeines = list(map(int, input().split()))

dp = [INF] * (k+1)
dp[0] = 0
for c in caffeines:
    for w in range(k, c-1, -1):
        dp[w] = min(dp[w], dp[w-c]+1)

print(dp[k] if dp[k] != INF else -1)