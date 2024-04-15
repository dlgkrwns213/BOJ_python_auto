# https://www.acmicpc.net/problem/14618
import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = float('inf')


def dijkstra():
    distances = [INF] * (n+1)
    distances[j] = 0

    hq = []
    heappush(hq, (0, 0, j))

    while hq:
        dist, color, now = heappop(hq)
        if distances[now] < dist:
            continue

        if color:
            return f'{"A" if color == 1 else "B"}\n{distances[now]}'

        for nxt, nd in graph[now]:
            nxt_dist = nd + dist
            if distances[nxt] > nxt_dist:
                distances[nxt] = nxt_dist
                heappush(hq, (nxt_dist, colors[nxt], nxt))

    return -1


n, m = map(int, input().split())
j = int(input())
input()
colors = [0] * (n+1)
for a in map(int, input().split()):
    colors[a] = 1
for b in map(int, input().split()):
    colors[b] = 2
graph: list[list[tuple]] = [[] for _ in range(n+1)]
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))
    graph[y].append((x, z))

print(dijkstra())