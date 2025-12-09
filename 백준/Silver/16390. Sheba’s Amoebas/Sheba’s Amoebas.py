import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, y):
    go = [(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1) if i or j]

    q = deque()
    q.append((x, y))

    visited[x][y] = True

    while q:
        x, y = q.popleft()
        for a, b in go:
            nx, ny = x+a, y+b

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if board[nx][ny] != '#' or visited[nx][ny]:
                continue

            visited[nx][ny] = True
            q.append((nx, ny))


n, m = map(int, input().split())
board = [input().rstrip() for _ in range(n)]

visited = [[False]*m for _ in range(n)]
count = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == '#' and not visited[i][j]:
            bfs(i, j)
            count += 1

print(count)