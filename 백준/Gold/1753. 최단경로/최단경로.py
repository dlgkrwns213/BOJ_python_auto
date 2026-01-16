import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = float('inf')


def dijkstra(start):
    distances = [INF] * (n+1)
    distances[start] = 0

    hq = []
    heappush(hq, (0, start))

    while hq:
        dist, now = heappop(hq)
        if distances[now] < dist:
            continue

        for nxt, nw in graph[now]:
            nxt_dist = nw + dist

            if distances[nxt] > nxt_dist:
                distances[nxt] = nxt_dist
                heappush(hq, (nxt_dist, nxt))

    return distances


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

start = int(input())
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    # graph[v].append((u, w))

answer = dijkstra(start)[1:]
print('\n'.join(map(lambda x: 'INF' if x == INF else str(x), answer)))