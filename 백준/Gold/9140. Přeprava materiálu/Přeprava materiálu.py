import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = float('inf')


def dijkstra():
    distances = [INF] * (n+1)
    distances[s] = 0

    hq = []
    heappush(hq, (0, s))

    while hq:
        dist, now = heappop(hq)
        if now == c:
            return dist
        if distances[now] < dist:
            continue

        for nxt, nd in graph[now]:
            nxt_dist = nd + dist
            if distances[nxt] > nxt_dist:
                distances[nxt] = nxt_dist
                heappush(hq, (nxt_dist, nxt))

    return -1


while True:
    n, m, s, c = map(int, input().split())
    if not n:
        break
        
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, v = map(int, input().split())
        graph[a].append((b, v))

    print(dijkstra())