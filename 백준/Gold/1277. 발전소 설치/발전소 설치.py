# https://www.acmicpc.net/problem/1277
import sys
from heapq import heappop, heappush
from math import sqrt
input = sys.stdin.readline
INF = float('inf')


def dijkstra():
    distances = [INF] * n
    distances[0] = 0

    hq = []
    heappush(hq, (0, 0))

    while hq:
        dist, now = heappop(hq)
        if now == n-1:
            return int(dist * 1000)

        if distances[now] < dist:
            continue

        for nxt, nd in graph[now]:
            nxt_dist = nd + dist
            if distances[nxt] > nxt_dist:
                distances[nxt] = nxt_dist
                heappush(hq, (nxt_dist, nxt))

    return INF


n, w = map(int, input().split())
m = float(input())
locations = [list(map(int, input().split())) for _ in range(n)]
connected = {tuple(map(int, input().split())) for _ in range(w)}

graph = [[] for _ in range(n)]
for i, ixy in enumerate(locations):
    ix, iy = ixy
    for j, jxy in enumerate(locations):
        jx, jy = jxy
        if i == j:
            continue
        if (i+1, j+1) in connected:
            graph[i].append((j, 0))
            graph[j].append((i, 0))
            continue

        length = sqrt((ix - jx) ** 2 + (iy - jy) ** 2)
        if length <= m:
            graph[i].append((j, length))
            graph[j].append((i, length))

ans = dijkstra()
print(ans if ans != INF else -1)