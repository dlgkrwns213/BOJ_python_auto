# https://www.acmicpc.net/problem/17485
import sys
input = sys.stdin.readline
INF = float('inf')

n, m = map(int, input().split())
costs = [list(map(int, input().split())) for _ in range(n)]

dp = [[[INF]*3 for _ in range(m+1)] for _ in range(n)]
for j in range(m):
    dp[0][j] = [costs[0][j]] * 3

for i in range(1, n):
    for j in range(m):
        la, lb, lc = dp[i-1][j-1]
        ma, mb, mc = dp[i-1][j]
        ra, rb, rc = dp[i-1][j+1]

        dp[i][j][0] = min(lb, lc) + costs[i][j]
        dp[i][j][1] = min(ma, mc) + costs[i][j]
        dp[i][j][2] = min(ra, rb) + costs[i][j]

print(min(map(min, dp[-1])))