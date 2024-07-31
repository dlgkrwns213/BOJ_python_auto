# https://www.acmicpc.net/problem/30508
import sys
from collections import deque
input = sys.stdin.readline


def bfs(sx, sy):
    if not heights[sx][sy]:
        return

    go = ((-1, 0), (1, 0), (0, -1), (0, 1))

    q = deque()
    q.append((sx, sy, heights[sx][sy]))

    heights[sx][sy] = 0

    while q:
        x, y, now = q.popleft()
        for a, b in go:
            nx, ny = x+a, y+b
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            nxt = heights[nx][ny]
            if nxt and nxt >= now:
                heights[nx][ny] = 0
                q.append((nx, ny, nxt))


n, m = map(int, input().split())
h, w = map(int, input().split())
heights = [list(map(int, input().split())) for _ in range(n)]
k = int(input())
for _ in range(k):
    r, c = map(int, input().split())
    bfs(r-1, c-1)

prefix = [[0]*(m+1) for _ in range(n+1)]
for i in range(n):
    for j in range(m):
        prefix[i+1][j+1] = prefix[i+1][j] + prefix[i][j+1] - prefix[i][j] + (1 if heights[i][j] else 0)

cnt = 0
for i in range(n-h+1):
    for j in range(m-w+1):
        if not prefix[i+h][j+w] - prefix[i+h][j] - prefix[i][j+w] + prefix[i][j]:
            cnt += 1

print(cnt)