# https://www.acmicpc.net/problem/21924
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


n, m = map(int, input().split())
costs = [list(map(int, input().split())) for _ in range(m)]
costs.sort(key=lambda cost: cost[2])

parent, rank, total, need = list(range(n+1)), [1] * (n+1), 0, 0
for a, b, c in costs:
    total += c
    if find(a) != find(b):
        union(a, b)
        need += c

one = find(1)
print(total-need if all(find(node) == one for node in range(2, n+1)) else -1)