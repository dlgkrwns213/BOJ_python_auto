# https://www.acmicpc.net/problem/16132
import sys
input = sys.stdin.readline

n = int(input())
total = n * (n+1) >> 1

if total & 1:
    print(0)
    exit(0)

find = total >> 1;
dp = [[0]*(find+1) for _ in range(n+1)]

dp[0][0] = 1
for i in range(1, n+1):
    for j in range(find+1):
        dp[i][j] += dp[i-1][j] + (dp[i-1][j-i] if j >= i else 0)

print(dp[n][find] >> 1)