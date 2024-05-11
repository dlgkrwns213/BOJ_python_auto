# https://www.acmicpc.net/problem/5944
import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = float('inf')


def dijkstra():
    distances = [[INF] * 4 for _ in range(p+1)]
    distances[pb][0] = 0

    hq = []
    heappush(hq, (0, 0, pb))

    while hq:
        dist, reach, now = heappop(hq)
        if reach == 3:
            return dist

        if distances[now][reach] < dist:
            continue

        for nxt, nd in graph[now]:
            nxt_dist = nd + dist
            nxt_reach = reach
            if nxt in idx:
                nxt_reach |= 1 << idx[nxt]

            if distances[nxt][nxt_reach] > nxt_dist:
                distances[nxt][nxt_reach] = nxt_dist
                heappush(hq, (nxt_dist, nxt_reach, nxt))

    return INF


c, p, pb, pa1, pa2 = map(int, input().split())
graph = [[] for _ in range(p+1)]
for _ in range(c):
    p1, p2, d = map(int, input().split())
    graph[p1].append((p2, d))
    graph[p2].append((p1, d))

idx = {pa1: 0, pa2: 1}
print(dijkstra())