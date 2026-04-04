MOD = 10**9 + 7

n, k = map(int, input().split())

dp = [[0]*(k+1) for _ in range(n)]
dp[0] = [0] + [1]*k
for i in range(1, n):
    total = sum(dp[i-1])

    for j in range(1, k+1):
        dp[i][j] = total

        for x in range(2*j, k+1, j):
            dp[i][j] -= dp[i-1][x]
            dp[i][j] %= MOD

print(sum(dp[-1]) % MOD)