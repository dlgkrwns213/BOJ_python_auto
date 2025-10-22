from collections import deque
go = [(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1) if i or j]


def dfs(x, y):
    visited[x][y] = True
    for a, b in go:
        nx, ny = x+a, y+b
        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue
        if board[nx][ny] != '#' or visited[nx][ny]:
            continue

        dfs(nx, ny)


m, n = map(int, input().split())
board = [input().rstrip() for _ in range(m)]

visited = [[False]*n for _ in range(m)]
count = 0
for i in range(m):
    for j in range(n):
        if board[i][j] == '#' and not visited[i][j]:
            count += 1
            dfs(i, j)

print(count)