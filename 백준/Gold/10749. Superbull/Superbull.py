# https://www.acmicpc.net/problem/10749
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


n = int(input())
teams = [int(input()) for _ in range(n)]

values = [(ia, ib, va^vb) for ia, va in enumerate(teams) for ib, vb in enumerate(teams[:ia])]
values.sort(key=lambda value: -value[2])

parent, rank = list(range(n)), [1] * n
total = 0
for a, b, v in values:
    if find(a) != find(b):
        union(a, b)
        total += v
print(total)