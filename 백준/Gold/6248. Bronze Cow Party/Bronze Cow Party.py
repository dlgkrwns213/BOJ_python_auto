# https://www.acmicpc.net/problem/6248
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
INF = float('inf')


def dijkstra():
    distances = [INF] * (n+1)
    distances[x] = 0

    hq = []
    heappush(hq, (0, x))

    while hq:
        dist, now = heappop(hq)
        if distances[now] < dist:
            continue

        for nxt, nd in graph[now]:
            nxt_dist = nd + dist
            if distances[nxt] > nxt_dist:
                distances[nxt] = nxt_dist
                heappush(hq, (nxt_dist, nxt))

    return max(distances[1:])


n, m, x = map(int, input().split())
graph: list[list[tuple]] = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    graph[b].append((a, t))

ans = dijkstra()
print(ans << 1)