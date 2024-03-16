# https://www.acmicpc.net/problem/1749

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

prefix_col = [[0]*m for _ in range(n+1)]
for j in range(m):
    for i in range(1, n+1):
        prefix_col[i][j] = prefix_col[i-1][j] + board[i-1][j]

mx = -float('inf')
for ia in range(1, n+1):
    for ib in range(ia):
        now = 0
        for j in range(m):
            now += prefix_col[ia][j] - prefix_col[ib][j]
            mx = max(mx, now)
            if now < 0:
                now = 0

print(mx)