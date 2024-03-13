# https://www.acmicpc.net/problem/20183
import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = float('inf')


def dijkstra(mx):
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

        for nxt, nc in graph[now]:
            if nc > mx:
                continue

            nxt_cost = nc + cost
            if nxt_cost > init_money:
                continue

            if costs[nxt] > nxt_cost:
                costs[nxt] = nxt_cost
                heappush(hq, (nxt_cost, nxt))

    return False


n, m, start, destination, init_money = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))

left, right = 1, init_money+1
while left < right:
    mid = left + right >> 1
    if dijkstra(mid):
        right = mid
    else:
        left = mid + 1

print(left if left <= init_money else -1)