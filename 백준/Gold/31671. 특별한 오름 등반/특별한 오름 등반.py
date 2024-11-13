# https://www.acmicpc.net/problem/31671
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dp = [[-2]*(2*n+2) for _ in range(n+2)]
for i in range(n+1):
    for j in range(i, 2*n+1-i):
        dp[i][j] = -1
for _ in range(m):
    x, y = map(int, input().split())
    dp[y][x] = -2

dp[0][0] = 0
for j in range(1, 2*n+1):
    for i in range(n+1):
        if dp[i][j] == -1:
            dp[i][j] = dp[i+1][j-1]
            if dp[i-1][j-1] >= 0:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1], i)

print(dp[0][2*n] if dp[0][2*n] >= 0 else -1)