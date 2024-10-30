# https://www.acmicpc.net/problem/14925
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(lambda x: 1 if x == '0' else 0, input().split())) for _ in range(n)]

dp = [[0]*(m+1) for _ in range(n+1)]
for i in range(n):
    for j in range(m):
        if board[i][j]:
            dp[i+1][j+1] = min(dp[i+1][j], dp[i][j+1], dp[i][j]) + 1

print(max(map(max, dp)))