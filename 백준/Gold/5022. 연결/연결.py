# https://www.acmicpc.net/problem/5022
from collections import deque
INF = float('inf')


def bfs(s1, d1, s2, d2):
    go = ((-1, 0), (1, 0), (0, -1), (0, 1))

    s1x, s1y = s1
    d1x, d1y = d1
    s2x, s2y = s2
    d2x, d2y = d2

    log = [[-1]*(m+1) for _ in range(n+1)]
    log[s2x][s2y] = -2
    log[d2x][d2y] = -2

    q = deque()
    q.append((s1x, s1y))

    while q:
        x, y = q.popleft()
        if (x, y) == (d1x, d1y):
            break

        for idx, val in enumerate(go):
            a, b = val
            nx, ny = x+a, y+b
            if nx < 0 or nx > n or ny < 0 or ny > m:
                continue
            if log[nx][ny] != -1:
                continue

            log[nx][ny] = idx
            q.append((nx, ny))

    visited = [[0]*(m+1) for _ in range(n+1)]
    visited[d1x][d1y] = 1

    ret = 0
    x, y = d1x, d1y
    while (x, y) != (s1x, s1y):
        a, b = go[log[x][y]]
        x -= a
        y -= b
        visited[x][y] = 1
        ret += 1

    q = deque()
    q.append((s2x, s2y, ret))

    while q:
        x, y, ret = q.popleft()
        if (x, y) == (d2x, d2y):
            return ret

        for a, b in go:
            nx, ny = x+a, y+b
            if nx < 0 or nx > n or ny < 0 or ny > m:
                continue
            if visited[nx][ny]:
                continue

            visited[nx][ny] = 1
            q.append((nx, ny, ret+1))
    return INF


n, m = map(int, input().split())
a1 = tuple(map(int, input().split()))
b1 = tuple(map(int, input().split()))
a2 = tuple(map(int, input().split()))
b2 = tuple(map(int, input().split()))

ans = min(bfs(a1, b1, a2, b2), bfs(a2, b2, a1, b1))
print(ans if ans != INF else 'IMPOSSIBLE')