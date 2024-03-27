# https://www.acmicpc.net/problem/20160
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
INF = float('inf')


def dijkstra(start, destination):
    distances = [INF] * (v+1)
    distances[start] = 0

    hq = []
    heappush(hq, (0, start))

    while hq:
        dist, now = heappop(hq)
        if now == destination:
            return dist
        if distances[now] < dist:
            continue

        for nxt, nd in graph[now]:
            nxt_dist = nd + dist
            if distances[nxt] > nxt_dist:
                distances[nxt] = nxt_dist
                heappush(hq, (nxt_dist, nxt))

    return INF


v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))

locations = list(map(int, input().split()))

seller, seller_time, seller_start = [0], 0, 0
for i in range(1, 10):
    now = dijkstra(locations[seller_start], locations[i])
    if now == INF:
        seller.append(-1)
    else:
        seller_time += now
        seller.append(seller_time)
        seller_start = i

b = int(input())
buyer = list(map(lambda i: dijkstra(b, locations[i]), range(10)))

first = -1
for i in range(10):
    if seller[i] >= buyer[i]:
        first = i
        break

if first == -1:
    print(-1)
else:
    print(min(locations[first:]))