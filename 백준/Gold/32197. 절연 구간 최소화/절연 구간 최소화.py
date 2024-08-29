# https://www.acmicpc.net/problem/32197
import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    q = deque()
    q.append((start, -1, 0))

    visited = [0] * 2*(n+1)

    while q:
        now, dt, cnt = q.popleft()
        if now == destination:
            return cnt

        for nxt, nt in graph[now]:
            nxt_idx = nt * (n+1) + nxt
            if visited[nxt_idx]:
                continue

            visited[nxt_idx] = True
            if dt == nt:
                q.appendleft((nxt, nt, cnt))
            else:
                q.append((nxt, nt, cnt+1))

    return float('inf')


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, t = map(int, input().split())
    graph[s].append((e, t))
    graph[e].append((s, t))

start, destination = map(int, input().split())
print(bfs()-1)