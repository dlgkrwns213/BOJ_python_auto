import sys
from collections import deque
input = sys.stdin.readline
MAX = 1002


def bfs():
    go = ((-1, 0), (1, 0), (0, -1), (0, 1))

    q = deque()
    q.append((501, 501, 0))

    visited[501][501] = 1

    while q:
        x, y, d = q.popleft()
        if (x, y) == (dx, dy):
            return d

        for a, b in go:
            nx, ny = x+a, y+b
            if nx < 0 or nx > MAX or ny < 0 or ny > MAX:
                continue
            if visited[nx][ny]:
                continue

            visited[nx][ny] = 1
            q.append((nx, ny, d+1))


dx, dy, n = map(int, input().split())
dx, dy = map(lambda m: m+501, (dx, dy))
visited = [[0]*(MAX+1) for _ in range(MAX)]
for _ in range(n):
    a, b = map(lambda m: int(m)+501, input().split())
    visited[a][b] = -1

print(bfs())