# https://www.acmicpc.net/problem/10776
import sys
from heapq import heappop, heappush
input = sys.stdin.readline


def dijkstra():
    INF = float('inf')

    times = [[INF]*k for _ in range(n+1)]
    times[start][0] = 0

    hq = []
    heappush(hq, (0, 0, start))

    while hq:
        time, height, now = heappop(hq)
        if now == destination:
            return time
        if times[now][height] < time:
            continue

        for nxt, nt, nh in graph[now]:
            nxt_time = nt + time
            nxt_height = nh + height

            if nxt_height >= k:
                continue
            if times[nxt][nxt_height] > nxt_time:
                times[nxt][nxt_height] = nxt_time
                heappush(hq, (nxt_time, nxt_height, nxt))
    return -1


k, n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, t, h = map(int, input().split())
    graph[a].append((b, t, h))
    graph[b].append((a, t, h))

start, destination = map(int, input().split())
print(dijkstra())