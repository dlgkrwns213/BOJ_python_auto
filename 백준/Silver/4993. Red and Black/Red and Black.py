import sys
from collections import deque
input = sys.stdin.readline


def get_start():
    for i in range(n):
        for j in range(m):
            if board[i][j] == '@':
                return i, j


def bfs(sx, sy):
    go = ((-1, 0), (1, 0), (0, -1), (0, 1))

    visited = [[False]*m for _ in range(n)]
    visited[sx][sy] = True

    q = deque()
    q.append((sx, sy))

    count = 0
    while q:
        x, y = q.popleft()
        count += 1

        for a, b in go:
            nx, ny = x+a, y+b
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if board[nx][ny] == '#' or visited[nx][ny]:
                continue

            visited[nx][ny] = True
            q.append((nx, ny))

    return count


while True:
    m, n = map(int, input().split())
    if not n and not m:
        break

    board = [input().rstrip() for _ in range(n)]
    print(bfs(*get_start()))