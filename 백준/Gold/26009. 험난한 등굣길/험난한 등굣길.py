# https://www.acmicpc.net/problem/26009
import sys
from collections import deque
input = sys.stdin.readline


def draw(x, y):
    if 0 <= x < n and 0 <= y < m:
        board[x][y] = 1


def bfs():
    go = ((-1, 0), (1, 0), (0, -1), (0, 1))

    visited = [[0]*m for _ in range(n)]
    visited[0][0] = 1

    q = deque()
    q.append((0, 0, 0))

    while q:
        x, y, cnt = q.popleft()
        if (x, y) == (n-1, m-1):
            return cnt

        for a, b in go:
            nx, ny = x+a, y+b
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if board[nx][ny] or visited[nx][ny]:
                continue

            visited[nx][ny] = 1
            q.append((nx, ny, cnt+1))

    return -1


n, m = map(int, input().split())
board = [[0]*m for _ in range(n)]
for _ in range(int(input())):
    r, c, d = map(int, input().split())
    r, c = map(lambda z: z-1, (r, c))

    board[r][c] = 1
    for i in range(d):
        draw(r-d+i, c+i)
    for i in range(d):
        draw(r+i, c+d-i)
    for i in range(d):
        draw(r+d-i, c-i)
    for i in range(d):
        draw(r-i, c-d+i)

ans = bfs()
print(f'YES\n{ans}' if ans != -1 else 'NO')