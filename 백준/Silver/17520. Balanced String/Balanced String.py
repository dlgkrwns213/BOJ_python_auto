MOD = 16769023

n = int(input())
dp = [[0]*3 for _ in range(n)]
dp[0] = [0, 1, 1]

for i in range(1, n):
    dp[i][1] = dp[i-1][0]
    dp[i][0] = (dp[i-1][-1] + dp[i-1][1]) % MOD
    dp[i][-1] = dp[i-1][0]

print(sum(dp[-1]) % MOD)