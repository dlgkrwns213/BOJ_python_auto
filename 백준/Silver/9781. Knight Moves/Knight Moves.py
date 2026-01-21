import sys
from collections import deque
input = sys.stdin.readline


def find(x):
    for i in range(n):
        for j in range(m):
            if board[i][j] == x:
                return i, j


def bfs(sx, sy, dx, dy):
    go = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))

    q = deque()
    q.append((sx, sy, 0))

    visited = [[board[i][j] == '#' for j in range(m)] for i in range(n)]
    visited[sx][sy] = True

    while q:
        x, y, cnt = q.popleft()
        if (x, y) == (dx, dy):
            return cnt

        for a, b in go:
            nx, ny = x+a, y+b
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited[nx][ny]:
                continue

            visited[nx][ny] = True
            q.append((nx, ny, cnt+1))
    return -1


n, m = map(int, input().split())
board = [input().rstrip() for _ in range(n)]

print(bfs(*find('K'), *find('X')))