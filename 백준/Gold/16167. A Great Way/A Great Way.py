# https://www.acmicpc.net/problem/16167
import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = float('inf')


def dijkstra():
    distances = [INF] * (n+1)
    distances[1] = 1

    hq = []
    heappush(hq, (1, 1))

    while hq:
        weight, now = heappop(hq)
        if distances[now] < weight:
            continue
        dist, cnt = divmod(weight, 101)
        if now == n:
            return dist, cnt

        for nxt, nd in graph[now]:
            nxt_dist = nd + dist
            nxt_weight = (nxt_dist * 101) + cnt + 1
            if distances[nxt] > nxt_weight:
                distances[nxt] = nxt_weight
                heappush(hq, (nxt_weight, nxt))

    return INF, INF


n, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(r):
    a, b, c, d, e = map(int, input().split())
    w = c + (d * (e - 10) if e >= 10 else 0)
    graph[a].append((b, w))

total, count = dijkstra()
if total == INF:
    print('It is not a great way.')
else:
    print(total, count)