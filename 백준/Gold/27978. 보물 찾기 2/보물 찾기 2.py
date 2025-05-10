# https://www.acmicpc.net/problem/27978
import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')


def find(x: str):
    for i in range(n):
        for j in range(m):
            if board[i][j] == x:
                return i, j


def bfs():
    go = [(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1) if i or j]

    visited = [[INF]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] == '#':
                visited[i][j] = -INF
    visited[sx][sy] = 0

    q = deque()
    q.append((sx, sy, 0))

    while q:
        x, y, cnt = q.popleft()
        if (x, y) == (dx, dy):
            return cnt

        for a, b in go:
            nx, ny = x + a, y + b
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if b == 1:
                if visited[nx][ny] > cnt:
                    visited[nx][ny] = cnt
                    q.appendleft((nx, ny, cnt))
            else:
                if visited[nx][ny] > cnt + 1:
                    visited[nx][ny] = cnt+1
                    q.append((nx, ny, cnt+1))

    return -1


n, m = map(int, input().split())
board = [input().rstrip() for _ in range(n)]

sx, sy = find('K')
dx, dy = find('*')

print(bfs())