# https://www.acmicpc.net/problem/1229
hexas = [i * (2*i-1) for i in range(1, 750)]

n = int(input())

dp = [7] * (n+1)
dp[0] = 0
for i in range(1, n+1):
    mn = 7
    for hexa in hexas:
        if hexa > i:
            break

        mn = min(mn, dp[i-hexa] + 1)
    dp[i] = mn

print(dp[n])