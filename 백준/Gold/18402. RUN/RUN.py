# https://www.acmicpc.net/problem/18402
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
INF = float('inf')


def dijkstra():
    distances = [INF] * (n+1)
    distances[1] = 0

    hq = []
    heappush(hq, (0, 1))

    while hq:
        dist, now = heappop(hq)

        if distances[now] < dist:
            continue

        for nxt, nd in graph[now]:
            nxt_dist = nd + dist

            if distances[nxt] > nxt_dist:
                distances[nxt] = nxt_dist
                heappush(hq, (nxt, nxt_dist))

    return distances



n = int(input())
e = int(input())
t = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(int(input())):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))

distances = dijkstra()
print(sum(map(lambda node: distances[node] <= t, range(1, n+1))))