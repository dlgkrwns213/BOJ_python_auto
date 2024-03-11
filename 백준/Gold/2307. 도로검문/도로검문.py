# https://www.acmicpc.net/problem/2307
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
INF = float('inf')


def get_route() -> (list, int):
    distances = [INF] * (n+1)
    distances[1] = 0

    hq = []
    heappush(hq, (0, 1))

    log = [-1] * (n+1)
    while hq:
        dist, now = heappop(hq)
        if distances[now] < dist:
            continue

        for nxt, nd in graph[now]:
            nxt_dist = nd + dist
            if distances[nxt] > nxt_dist:
                distances[nxt] = nxt_dist
                heappush(hq, (nxt_dist, nxt))
                log[nxt] = now

    now, route = n, []
    while now != -1:
        route.append(now)
        now = log[now]

    return route[::-1], distances[n]


def dijkstra(check: tuple):
    distances = [INF] * (n+1)
    distances[1] = 0

    hq = []
    heappush(hq, (0, 1))

    log = [-1] * (n+1)
    while hq:
        dist, now = heappop(hq)
        if distances[now] < dist:
            continue

        for nxt, nd in graph[now]:
            if (now, nxt) == check or (nxt, now) == check:
                continue
            nxt_dist = nd + dist
            if distances[nxt] > nxt_dist:
                distances[nxt] = nxt_dist
                heappush(hq, (nxt_dist, nxt))
                log[nxt] = now

    return distances[n]


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    graph[b].append((a, t))

shortest_route, shortest_distance = get_route()

mx = shortest_distance
for i in range(len(shortest_route)-1):
    mx = max(mx, dijkstra((shortest_route[i], shortest_route[i+1])))

print(mx-shortest_distance if mx != INF else -1)