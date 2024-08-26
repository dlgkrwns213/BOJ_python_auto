# https://www.acmicpc.net/problem/2350
import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')


def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x, y = map(find, (x, y))

    if rank[x] >= rank[y]:
        rank[x] += rank[y]
        parent[y] = x
    else:
        rank[y] += rank[x]
        parent[x] = y


def bfs(start, destination):
    q = deque()
    q.append((start, -1, INF))

    while q:
        now, bef, mn = q.popleft()
        if now == destination:
            return mn

        for nxt, nw in graph[now]:
            if nxt == bef:
                continue

            q.append((nxt, now, min(mn, nw)))

    return INF


n, m, k = map(int, input().split())
canals = [list(map(int, input().split())) for _ in range(m)]
canals.sort(key=lambda canal: -canal[2])

parent, rank = list(range(n+1)), [1] * (n+1)
graph = [[] for _ in range(n+1)]
for i, j, w in canals:
    if find(i) != find(j):
        union(i, j)
        graph[i].append((j, w))
        graph[j].append((i, w))

ans = []
for _ in range(k):
    i, j = map(int, input().split())
    ans.append(bfs(i, j))

print('\n'.join(map(str, ans)))