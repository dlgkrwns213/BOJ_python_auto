# https://www.acmicpc.net/problem/20182
import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = float('inf')
MOD = (1 << 18) - 1


def dijkstra(start, destination, init_money):
    costs = [INF] * (n+1)
    costs[start] = 0
    
    hq = []
    heappush(hq, (0, start))
    
    while hq:
        cost, now = heappop(hq)
        if now == destination:
            return cost >> 18
        if costs[now] < cost:
            continue

        mx = cost >> 18
        total = cost & MOD
        for nxt, nm in graph[now]:
            nxt_total = total + nm
            if nxt_total > init_money:
                continue

            nxt_cost = (max(mx, nm) << 18) | nxt_total
            if costs[nxt] > nxt_cost:
                costs[nxt] = nxt_cost
                heappush(hq, (nxt_cost, nxt))

    return -1


n, m, a, b, c = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))
    
print(dijkstra(a, b, c))