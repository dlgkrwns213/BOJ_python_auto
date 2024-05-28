# https://www.acmicpc.net/problem/20182
import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = float('inf')
MOD = (1 << 18) - 1


def dijkstra(start, destination, init_cost, mx_money):
    costs = [INF] * (n+1)
    costs[start] = 0
    
    hq = []
    heappush(hq, (0, start))

    while hq:
        cost, now = heappop(hq)
        if now == destination:
            return True
        if costs[now] < cost:
            continue

        for nxt, nm in graph[now]:
            if nm > mx_money:
                continue

            nxt_cost = nm + cost
            if nxt_cost > init_cost:
                continue
            if costs[nxt] > nxt_cost:
                costs[nxt] = nxt_cost
                heappush(hq, (nxt_cost, nxt))

    return False


n, m, a, b, c = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

left, right = 1, 21
while left < right:
    mid = left + right >> 1
    if dijkstra(a, b, c, mid):
        right = mid
    else:
        left = mid + 1

print(left if left != 21 else -1)