# https://www.acmicpc.net/problem/23801
import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = float('inf')


def dijkstra():
    distances = [[INF] * 2 for _ in range(n+1)]
    distances[x][0] = 0

    hq = []
    heappush(hq, (0, x, 0))

    while hq:
        dist, now, check = heappop(hq)
        if distances[now][check] < dist:
            continue

        for nxt, nd in graph[now]:
            nxt_dist = nd + dist
            nxt_check = check | (nxt in y)
            if distances[nxt][nxt_check] > nxt_dist:
                distances[nxt][nxt_check] = nxt_dist
                heappush(hq, (nxt_dist, nxt, nxt_check))

                if nxt_check and distances[nxt][0] > distances[nxt][1]:
                    distances[nxt][0] = distances[nxt][1]

    return distances[z][1]


n, m = map(int, input().split())
graph: list[list[tuple]] = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

x, z = map(int, input().split())
p = int(input())
y = set(map(int, input().split()))

ans = dijkstra()
print(ans if ans != INF else -1)