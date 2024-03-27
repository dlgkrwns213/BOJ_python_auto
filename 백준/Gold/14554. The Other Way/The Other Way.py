# https://www.acmicpc.net/problem/14554
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
INF = float('inf')
MOD = int(1e9) + 9


def dijkstra():
    distances = [INF] * (n+1)
    distances[s] = 0

    dp = [0] * (n+1)
    dp[s] = 1

    hq = []
    heappush(hq, (0, s))

    while hq:
        dist, now = heappop(hq)
        if distances[now] < dist:
            continue

        for nxt, nd in graph[now]:
            nxt_dist = nd + dist

            if distances[nxt] > nxt_dist:
                distances[nxt] = nxt_dist
                dp[nxt] = dp[now]
                heappush(hq, (nxt_dist, nxt))
            elif distances[nxt] == nxt_dist:
                dp[nxt] = (dp[nxt] + dp[now]) % MOD

    return dp[e]


n, m, s, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

print(dijkstra())