# https://www.acmicpc.net/problem/11084
from collections import deque


def bfs():
    go = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))
    MOD = int(1e9) + 9

    q = deque()
    q.append(0)

    steps = [-1] * r*c
    steps[0] = 0

    counts = [1] * r*c

    while q:
        now = q.popleft()
        
        x, y = divmod(now, c)
        if (x, y) == (r-1, c-1):
            return steps[now], counts[now]

        for a, b in go:
            nx, ny = x+a, y+b
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue

            nxt = nx * c + ny
            if steps[nxt] == -1:
                steps[nxt] = steps[now] + 1
                counts[nxt] = counts[now]
                q.append(nxt)
            elif steps[nxt] == steps[now] + 1:
                counts[nxt] = (counts[nxt] + counts[now]) % MOD

    return None,


r, c = map(int, input().split())
print(*bfs())