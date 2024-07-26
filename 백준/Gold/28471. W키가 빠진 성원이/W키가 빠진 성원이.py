# https://www.acmicpc.net/problem/28471
import sys
from collections import deque
input = sys.stdin.readline


def find_f():
    for i, line in enumerate(board):
        for j, v in enumerate(line):
            if v == 'F':
                return i, j


def bfs(sx, sy):
    go = [(-1, -1), (0, -1), (1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]

    q = deque()
    q.append((sx, sy))

    visited = [[0]*n for _ in range(n)]
    visited[sx][sy] = 1

    while q:
        x, y = q.popleft()
        for a, b in go:
            nx, ny = x+a, y+b
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if board[nx][ny] != '.' or visited[nx][ny]:
                continue

            visited[nx][ny] = 1
            q.append((nx, ny))

    return sum(map(sum, visited)) - 1


n = int(input())
board = [input().rstrip() for _ in range(n)]

sx, sy = find_f()
print(bfs(sx, sy))