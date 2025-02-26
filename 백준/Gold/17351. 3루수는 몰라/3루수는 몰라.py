# https://www.acmicpc.net/problem/17351
import sys
input = sys.stdin.readline
WORD = "MOLA"

n = int(input())
board = [input().rstrip() for _ in range(n)]

dp = [[0]*(n+1) for _ in range(n+1)]
for i in range(n):
    for j in range(n):
        up_n, up_r = divmod(dp[i-1][j], 4)
        left_n, left_r = divmod(dp[i][j-1], 4)

        now = board[i][j]
        if now == 'M':
            dp[i][j] = 4 * max(up_n, left_n) + 1
        else:
            up_r = (up_r + 1) if now == WORD[up_r] else 0
            left_r = (left_r + 1) if now == WORD[left_r] else 0

            dp[i][j] = max(4 * up_n + up_r, 4 * left_n + left_r)

print(dp[n-1][n-1] // 4)