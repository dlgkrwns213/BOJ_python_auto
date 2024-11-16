# https://www.acmicpc.net/problem/14221
import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = float('inf')


def dijkstra():
    input()
    homes = list(map(int, input().split()))

    distances = [INF] * (n+1)
    hq = []
    for start in map(int, input().split()):
        distances[start] = 0
        heappush(hq, (0, start))

    while hq:
        dist, now = heappop(hq)
        if distances[now] < dist:
            continue

        for nxt, nd in graph[now]:
            nxt_dist = nd + dist
            if distances[nxt] > nxt_dist:
                distances[nxt] = nxt_dist
                heappush(hq, (nxt_dist, nxt))

    mn = min(map(lambda home: distances[home], homes))
    return min(home for home in homes if distances[home] == mn)


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

print(dijkstra())