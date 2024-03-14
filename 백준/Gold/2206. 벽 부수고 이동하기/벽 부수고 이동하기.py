# https://www.acmicpc.net/problem/2206
import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    go = ((-1, 0), (1, 0), (0, -1), (0, 1))

    q = deque()
    q.append((0, 0, 0, 1))

    visited = [[2]*m for _ in range(n)]
    visited[0][0] = 0

    while q:
        x, y, broken_cnt, move = q.popleft()
        if (x, y) == (n-1, m-1):
            return move

        for a, b in go:
            nx, ny = x+a, y+b
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited[nx][ny] <= broken_cnt:
                continue

            if board[nx][ny] == '0':
                visited[nx][ny] = broken_cnt
                q.append((nx, ny, broken_cnt, move+1))
            elif board[nx][ny] == '1' and broken_cnt == 0:
                visited[nx][ny] = 1
                q.append((nx, ny, 1, move+1))
    return -1


n, m = map(int, input().split())
board = [input().rstrip() for _ in range(n)]
print(bfs())