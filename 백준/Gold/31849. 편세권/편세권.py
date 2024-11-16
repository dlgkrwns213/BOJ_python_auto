# https://www.acmicpc.net/problem/31849
import sys
from collections import deque
input = sys.stdin.readline
go = ((-1, 0), (1, 0), (0, -1), (0, 1))


def bfs():
    q = deque()

    for _ in range(c):
        b, d = map(int, input().split())
        q.append((b, d, 0))
        board[b][d] = -1

    while q:
        x, y, cnt = q.popleft()

        for a, b in go:
            nx, ny = x+a, y+b
            if nx <= 0 or nx > n or ny <= 0 or ny > m:
                continue
            if board[nx][ny]:
                continue

            board[nx][ny] = cnt + 1
            q.append((nx, ny, cnt+1))


n, m, r, c = map(int, input().split())
board = [[0]*(m+1) for _ in range(n+1)]
homes = [list(map(int, input().split())) for _ in range(r)]
bfs()

print(min(map(lambda home: board[home[0]][home[1]]*home[2], homes)))