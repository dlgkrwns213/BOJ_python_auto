import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    go = ((-1, 0), (1, 0), (0, -1), (0, 1))
    color = board[0][0]

    q = deque()
    q.append((0, 0))

    visited = [[0]*m for _ in range(n)]
    visited[0][0] = 1

    while q:
        x, y = q.popleft()
        if (x, y) == (n-1, m-1):
            return True

        for a, b in ((a, b) for a in range(-jump, jump+1) for b in range(-jump, jump+1) if abs(a)+abs(b) <= jump):
            nx, ny = x+a, y+b
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited[nx][ny] or board[nx][ny] != color:
                continue

            visited[nx][ny] = 1
            q.append((nx, ny))
    return False


n = int(input())
m = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
jump = int(input())

print('ALIVE' if bfs() else 'DEAD')