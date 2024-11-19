# https://www.acmicpc.net/problem/5558
import sys
from collections import deque
input = sys.stdin.readline
go = ((-1, 0), (1, 0), (0, -1), (0, 1))


def bfs(sx, sy, dx, dy):
    q = deque()
    q.append((sx, sy, 0))

    visited = list(map(lambda line: list(map(lambda b: 1 if b == 'X' else 0, line)), board))
    visited[sx][sy] = 1

    while q:
        x, y, cnt = q.popleft()
        if (x, y) == (dx, dy):
            return cnt

        for a, b in go:
            nx, ny = x+a, y+b
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if visited[nx][ny]:
                continue

            visited[nx][ny] = 1
            q.append((nx, ny, cnt+1))


def find() -> list:
    cheeses = [None] * (n+1)
    for i in range(h):
        for j in range(w):
            if board[i][j] == 'S':
                cheeses[0] = (i, j)
            elif board[i][j].isdigit():
                cheeses[int(board[i][j])] = (i, j)
    return cheeses


h, w, n = map(int, input().split())
board = [input().rstrip() for _ in range(h)]

cheeses = find()
print(sum(map(lambda idx: bfs(*cheeses[idx], *cheeses[idx+1]), range(n))))