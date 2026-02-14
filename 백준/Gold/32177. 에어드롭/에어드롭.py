import sys
from collections import deque
input = sys.stdin.readline


def can_deliver(x, y):
    xx, xy, xv = locations[x]
    yx, yy, yv = locations[y]

    return True if abs(xv-yv) <= t and (xx-yx) ** 2 + (xy-yy) ** 2 <= k*k else False


def bfs():
    q = deque()
    q.append(0)

    visited = [False] * (n+1)
    visited[0] = True

    pictures = []
    while q:
        now = q.popleft()
        if is_picture[now]:
            pictures.append(now)

        for nxt in graph[now]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)

    return pictures


n, k, t = map(int, input().split())

locations = []
is_picture = [0]
locations.append(list(map(int, input().split())))
for _ in range(n):
    *location, p = map(int, input().split())
    locations.append(location)
    is_picture.append(p)

graph = [[] for _ in range(n+1)]
for i in range(n+1):
    for j in range(i+1, n+1):
        if can_deliver(i, j):
            graph[i].append(j)
            graph[j].append(i)

answer = bfs()
print(' '.join(map(str, sorted(answer))) if answer else 0)