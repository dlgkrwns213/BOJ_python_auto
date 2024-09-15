import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    go = ((1, 0), (0, 1))

    q = deque()
    q.append((0, 0))

    visited = [[0]*n for _ in range(m)]
    visited[0][0] = 1

    while q:
        x, y = q.popleft()
        if (x, y) == (m-1, n-1):
            return True

        for a, b in go:
            nx, ny = x+a, y+b
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if not cities[nx][ny] or visited[nx][ny]:
                continue

            visited[nx][ny] = 1
            q.append((nx, ny))

    return False


n, m = map(int, input().split())
cities = [list(map(int, input().split())) for _ in range(m)]

print('Yes' if bfs() else 'No')