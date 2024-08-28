# https://www.acmicpc.net/problem/28119
import sys
input = sys.stdin.readline


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


n, m, s = map(int, input().split())
routes = [list(map(int, input().split())) for _ in range(m)]
routes.sort(key=lambda route: route[2])

parent, rank = list(range(n+1)), [1] * (n+1)
total = 0
for u, v, w in routes:
    if find(u) != find(v):
        union(u, v)
        total += w

print(total)