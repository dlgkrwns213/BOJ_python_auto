# https://www.acmicpc.net/problem/3482
import sys
from collections import deque
input = sys.stdin.readline
go = ((-1, 0), (1, 0), (0, -1), (0, 1))


def find_start_points():
    for i in range(r):
        for j in range(c):
            if board[i][j] == '.':
                return i, j


def bfs(sx, sy):
    visited = [[0 if board[i][j] == '.' else 1 for j in range(c)] for i in range(r)]
    visited[sx][sy] = 1

    q = deque()
    q.append((sx, sy, 0))

    x, y, cnt = sx, sy, 0
    while q:
        x, y, cnt = q.popleft()

        for a, b in go:
            nx, ny = x+a, y+b
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            if visited[nx][ny]:
                continue

            visited[nx][ny] = 1
            q.append((nx, ny, cnt+1))

    return x, y, cnt


ans = []
for _ in range(int(input())):
    c, r = map(int, input().split())
    board = [input().rstrip() for _ in range(r)]

    *xy, _ = bfs(*find_start_points())
    _, _, cnt = bfs(*xy)

    ans.append(cnt)

print('\n'.join(map(lambda length: f'Maximum rope length is {length}.', ans)))