# https://www.acmicpc.net/problem/17270
import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = sys.maxsize


def dijkstra(start):
    distances = [INF] * (v+1)
    distances[start] = 0

    hq = []
    heappush(hq, (0, start))

    while hq:
        dist, now = heappop(hq)
        if distances[now] < dist:
            continue

        for nxt, nd in graph[now]:
            nxt_dist = nd + dist
            if distances[nxt] > nxt_dist:
                distances[nxt] = nxt_dist
                heappush(hq, (nxt_dist, nxt))

    return distances


v, m = map(int, input().split())
graph = [[] for _ in range(v+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

j, s = map(int, input().split())
j_distances = dijkstra(j)
s_distances = dijkstra(s)

mn = min(map(lambda node: j_distances[node]+s_distances[node] if node not in (j, s) else INF, range(1, v+1)))
ans, min_dist = INF, INF
for node in range(1, v+1):
    if j_distances[node] + s_distances[node] == mn and j_distances[node] <= s_distances[node] and node not in (j, s):
        if j_distances[node] < min_dist:
            min_dist = j_distances[node]
            ans = node
        elif j_distances[node] == min_dist:
            ans = min(ans, node)
print(ans if ans != INF else -1)