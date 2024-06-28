# https://www.acmicpc.net/problem/1720
n = int(input())

dp = [0] * (n+2)
dp[1], dp[2] = 1, 3
for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2] * 2

if n == 1:
    print(1)
elif n == 2:
    print(3)
elif n % 2:
    print((dp[n] + dp[n >> 1]) // 2)
else:
    print((dp[n] + dp[n >> 1]) // 2 + dp[n-2 >> 1])