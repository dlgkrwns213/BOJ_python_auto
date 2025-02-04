# https://www.acmicpc.net/problem/12865
n, k = map(int, input().split())
things = [list(map(int, input().split())) for _ in range(n)]

dp = [0] * (k+1)
for w, v in things:
    for weight in range(k, w-1, -1):
        dp[weight] = max(dp[weight], dp[weight-w] + v)

print(dp[k])