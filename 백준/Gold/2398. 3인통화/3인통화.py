# https://www.acmicpc.net/problem/2398
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
INF = float('inf')


def dijkstra(start):
    distances = [INF] * (n+1)
    distances[start] = 0

    hq = []
    heappush(hq, (0, start))

    logs = [-1] * (n+1)
    while hq:
        dist, now = heappop(hq)
        if distances[now] < dist:
            continue

        for nxt, nd in graph[now]:
            nxt_dist = nd + dist
            if distances[nxt] > nxt_dist:
                distances[nxt] = nxt_dist
                heappush(hq, (nxt_dist, nxt))
                logs[nxt] = now

    return distances, logs


def get_route(destination, logs):
    route, now = [], destination
    while logs[now] != -1:
        route.append(tuple(sorted((logs[now], now))))
        now = logs[now]

    return route


n, m = map(int, input().split())
graph: list[list[tuple]] = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

a, b, c = map(int, input().split())

distances_a, logs_a = dijkstra(a)
distances_b, logs_b = dijkstra(b)
distances_c, logs_c = dijkstra(c)

distances = [distances_a[i] + distances_b[i] + distances_c[i] for i in range(n+1)]
min_locations = min(range(1, n+1), key=lambda i: distances[i])

route = get_route(min_locations, logs_a) + get_route(min_locations, logs_b) + get_route(min_locations, logs_c)
route = sorted(set(route))

print(distances[min_locations], len(route))
print('\n'.join(map(lambda line: ' '.join(map(str, line)), route)))