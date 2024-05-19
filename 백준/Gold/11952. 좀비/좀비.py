# https://www.acmicpc.net/problem/11952
import sys
from collections import deque
from heapq import heappop, heappush
input = sys.stdin.readline
INF = float('inf')


def bfs(zombies: list):
    deq = deque()
    for zombie in zombies:
        deq.append((zombie, 0))
        dangers[zombie] = 2

    while deq:
        now, dist = deq.popleft()
        if dist == s:
            return

        for nxt in graph[now]:
            if dangers[nxt]:
                continue

            dangers[nxt] = 1
            deq.append((nxt, dist+1))


def dijkstra() -> int or INF:
    costs = [INF] * (n+1)
    costs[1] = 0

    hq = []
    heappush(hq, (0, 1))

    while hq:
        cost, now = heappop(hq)
        if now == n:
            return cost - p
        if costs[now] < cost:
            continue

        for nxt in graph[now]:
            nxt_cost = cost + (p, q, INF)[dangers[nxt]]
            if costs[nxt] > nxt_cost:
                costs[nxt] = nxt_cost
                heappush(hq, (nxt_cost, nxt))
    return INF


n, m, k, s = map(int, input().split())
p, q = map(int, input().split())
zombies = [int(input()) for _ in range(k)]
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dangers = [0] * (n+1)
bfs(zombies)
dangers[n] = 0
print(dijkstra())