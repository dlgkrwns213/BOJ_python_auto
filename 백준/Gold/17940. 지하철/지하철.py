# https://www.acmicpc.net/problem/17940
import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = float('inf')
TRANS_WEIGHT = 1001


def dijkstra():
    costs = [INF] * n
    costs[0] = 0

    hq = []
    heappush(hq, (0, 0))

    while hq:
        cost, now = heappop(hq)
        if now == m:
            return divmod(cost, TRANS_WEIGHT)

        if costs[now] < cost:
            continue

        for nxt, nm in graph[now]:
            nxt_cost = cost + (TRANS_WEIGHT if company[now] != company[nxt] else 0) + nm
            if costs[nxt] > nxt_cost:
                costs[nxt] = nxt_cost
                heappush(hq, (nxt_cost, nxt))


n, m = map(int, input().split())
company = [int(input()) for _ in range(n)]
graph = [[] for _ in range(n)]
for i in range(n):
    for j, w in enumerate(map(int, input().split())):
        if w:
            graph[i].append((j, w))

print(*dijkstra())