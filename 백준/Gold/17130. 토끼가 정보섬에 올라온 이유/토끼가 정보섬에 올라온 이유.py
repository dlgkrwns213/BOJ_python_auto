# https://www.acmicpc.net/problem/17130
import sys
input = sys.stdin.readline
INF = float('inf')


def start():
    for j in range(m):
        for i in range(n):
            if board[i][j] == 'R':
                dp[i][j] = 0
                return j


n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]

dp = [[-INF]*m for _ in range(n+1)]
sj = start()

for j in range(sj+1, m):
    for i in range(n):
        if board[i][j] == '#':
            continue
        dp[i][j] = max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1]) + (1 if board[i][j] == 'C' else 0)

mx = max([dp[i][j] for j in range(m) for i in range(n) if board[i][j] == 'O'], default=-INF)
print(mx if mx != -INF else -1)