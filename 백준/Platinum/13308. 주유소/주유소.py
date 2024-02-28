# https://www.acmicpc.net/problem/13308
import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = float('inf')


# dijkstra
def get_distance(start):
    hq = []
    distances = [INF] * (n+1)

    heappush(hq, (0, start))
    distances[start] = 0

    while hq:
        now_dist, now = heappop(hq)
        if distances[now] < now_dist:
            continue

        for nxt, nd in graph[now]:
            nxt_dist = now_dist + nd
            if distances[nxt] > nxt_dist:
                distances[nxt] = nxt_dist
                heappush(hq, (nxt_dist, nxt))

    return distances


# dp + dfs
def get_cost(start):
    hq = []
    costs = [INF] * (n+1)
    dp = [INF] * (n+1)

    heappush(hq, (0, start, price[start]))
    costs[start] = 0
    dp[start] = price[start] * rest_distances[start]

    while hq:
        now_cost, now, min_cost = heappop(hq)

        for nxt, nd in graph[now]:
            nxt_cost = now_cost + nd * min_cost
            min_nxt_cost = min(min_cost, price[nxt])

            if costs[nxt] > nxt_cost:
                dp[nxt] = min(dp[nxt], nxt_cost + min_nxt_cost * rest_distances[nxt])
                costs[nxt] = nxt_cost
                heappush(hq, (nxt_cost, nxt, min_nxt_cost))

    return min(dp)



n, m = map(int, input().split())
price = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))

rest_distances = get_distance(n)  # 목적지까지 남은 거리

print(get_cost(1))