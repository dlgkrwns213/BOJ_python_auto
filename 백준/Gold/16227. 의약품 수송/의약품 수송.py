# https://www.acmicpc.net/problem/16227
import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = float('inf')


def dijkstra():
    times = [[INF]*101 for _ in range(n+2)]
    times[0][0] = 0

    hq = []
    heappush(hq, (0, 0, 0))  # 총 시간, 안 쉬고 달려온 시간, 위치

    while hq:
        time, once, now = heappop(hq)
        if now == n+1:
            return time

        if times[now][once] < time:
            continue

        for nxt, nt in graph[now]:
            nxt_time = nt + time

            # 이번 노드에서 쉬고 다음 노드로 이동
            if times[nxt][nt] > nxt_time + 5:
                times[nxt][nt] = nxt_time + 5
                heappush(hq, (nxt_time+5, nt, nxt))

            # 쉬지 않고 바로 이동
            nxt_once = once + nt
            if nxt_once > 100:
                continue
            if times[nxt][nxt_once] > nxt_time:
                times[nxt][nxt_once] = nxt_time
                heappush(hq, (nxt_time, nxt_once, nxt))
    return INF


n, k = map(int, input().split())
graph = [[] for _ in range(n+2)]
for _ in range(k):
    u, v, t = map(int, input().split())
    if t > 100:
        continue
    graph[u].append((v, t))
    graph[v].append((u, t))

print(dijkstra())