# https://www.acmicpc.net/problem/24042
import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = float('inf')


def dijkstra() -> int or INF:
    times = [INF] * (n+1)
    times[1] = 0

    hq = []
    heappush(hq, (0, 1))

    while hq:
        time, now = heappop(hq)
        if now == n:
            return time
        if times[now] < time:
            continue

        for nxt in graph[now]:
            earliest = min(map(lambda t: (t-time) % m, graph[now][nxt]))
            nxt_time = time + earliest + 1
            if times[nxt] > nxt_time:
                times[nxt] = nxt_time
                heappush(hq, (nxt_time, nxt))

    return INF


n, m = map(int, input().split())
graph = [dict() for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    if b not in graph[a]:
        graph[a][b] = []
    if a not in graph[b]:
        graph[b][a] = []

    graph[a][b].append(i)
    graph[b][a].append(i)

print(dijkstra())