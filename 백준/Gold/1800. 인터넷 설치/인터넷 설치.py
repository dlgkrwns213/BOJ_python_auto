# https://www.acmicpc.net/problem/1800
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
MAX = int(1e6)+1
INF = float('inf')


def dijkstra(mx):
    distances = [[INF] * (k+1) for _ in range(n+1)]
    distances[1][0] = 0

    hq = []
    heappush(hq, (0, 1, 0))

    while hq:
        price, now, free = heappop(hq)
        if now == n:
            return True
        if distances[now][free] < price:
            continue

        for nxt, np in graph[now]:
            if np > mx:
                if free == k:
                    continue
                if distances[nxt][free+1] > price:
                    distances[nxt][free+1] = price
                    heappush(hq, (price, nxt, free+1))
            else:
                nxt_price = max(price, np)
                if distances[nxt][free] > nxt_price:
                    distances[nxt][free] = nxt_price
                    heappush(hq, (nxt_price, nxt, free))

    return False


n, p, k = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(p):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))

left, right = 0, MAX
while left < right:
    mid = left + right >> 1
    if dijkstra(mid):
        right = mid
    else:
        left = mid + 1

print(left if left != MAX else -1)