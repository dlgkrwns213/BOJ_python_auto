# https://www.acmicpc.net/problem/2982
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
INF = float('inf')


def dijkstra(start, destination):
    distances = [INF] * (n+1)
    distances[start] = k

    hq = []
    heappush(hq, (k, start))

    while hq:
        dist, now = heappop(hq)
        if now == destination:
            return dist
        if distances[now] < dist:
            continue

        for nxt, nd in graph[now]:
            nxt_dist = nd + dist
            if (now, nxt) in cant:
                p, q = cant[(now, nxt)]
                if p < dist < q:
                    nxt_dist = q + nd

            if distances[nxt] > nxt_dist:
                distances[nxt] = nxt_dist
                heappush(hq, (nxt_dist, nxt))
    return INF


n, m = map(int, input().split())
a, b, k, g = map(int, input().split())
kings = list(map(int, input().split()))

graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, l = map(int, input().split())
    graph[u].append((v, l))
    graph[v].append((u, l))

cant, cant_time = dict(), 0
for i in range(g-1):
    now, nxt = kings[i], kings[i+1]
    time = -1
    for near, time in graph[now]:
        if near == nxt:
            cant[(now, nxt)] = (cant_time, cant_time+time)
            cant[(nxt, now)] = (cant_time, cant_time+time)
            cant_time += time
            break

print(dijkstra(a, b)-k)