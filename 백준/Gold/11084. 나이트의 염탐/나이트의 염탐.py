# https://www.acmicpc.net/problem/11084
from collections import deque


def bfs():
    go = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))
    MOD = int(1e9) + 9

    q = deque()
    q.append((0, 0))

    steps = [[-1]*c for _ in range(r)]
    steps[0][0] = 0

    counts = [[1]*c for _ in range(r)]

    while q:
        x, y = q.popleft()
        if (x, y) == (r-1, c-1):
            return steps[x][y], counts[x][y]

        for a, b in go:
            nx, ny = x+a, y+b
            if 0 <= nx < r and 0 <= ny < c:
                if steps[nx][ny] == -1:
                    steps[nx][ny] = steps[x][y] + 1
                    counts[nx][ny] = counts[x][y]
                    q.append((nx, ny))
                elif steps[nx][ny] == steps[x][y] + 1:
                    counts[nx][ny] = (counts[nx][ny] + counts[x][y]) % MOD

    return None,


r, c = map(int, input().split())
print(*bfs())