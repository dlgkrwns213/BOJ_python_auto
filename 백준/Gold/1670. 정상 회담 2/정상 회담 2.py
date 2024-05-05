# https://www.acmicpc.net/problem/1670
MOD = 987654321
n = int(input()) >> 1

dp = [0] * (n+3)
dp[0], dp[1], dp[2] = 1, 1, 2
for i in range(3, n+1):
    for j in range(i):
        dp[i] += dp[i-j-1] * dp[j]
    dp[i] %= MOD
print(dp[n])