# https://www.acmicpc.net/problem/5917
import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = float('inf')


def dijkstra(start, destination, init=False):
    distances = [INF] * (n+1)
    distances[start] = 0

    hq = []
    heappush(hq, (0, start))

    log = [-1] * (n+1)
    while hq:
        dist, now = heappop(hq)
        if now == destination and not init:
            return dist
        if distances[now] < dist:
            continue

        for nxt, nd in graph[now].items():
            nxt_dist = nd + dist
            if distances[nxt] > nxt_dist:
                distances[nxt] = nxt_dist
                log[nxt] = now
                heappush(hq, (nxt_dist, nxt))

    if init:
        route = []
        now = destination
        while now != -1:
            route.append(now)
            now = log[now]

        return route[::-1], distances[destination]

    return INF


n, m = map(int, input().split())
graph = [dict() for _ in range(n+1)]
for _ in range(m):
    a, b, l = map(int, input().split())
    graph[a][b] = l
    graph[b][a] = l

log, real = dijkstra(1, n, True)
mx = 0
for i, x in enumerate(log[:-1]):
    y = log[i+1]

    graph[x][y] <<= 1
    mx = max(mx, dijkstra(1, n) - real)
    graph[x][y] >>= 1

print(mx)