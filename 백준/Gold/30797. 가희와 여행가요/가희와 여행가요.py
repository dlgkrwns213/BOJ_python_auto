# https://www.acmicpc.net/problem/30797
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


n, q = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(q)]
roads.sort(key=lambda road: road[2]*int(1e9)+road[3])

parent, rank = list(range(n+1)), [1] * (n+1)
total_cost, mx_time = 0, 0
for a, b, cost, time in roads:
    if find(a) != find(b):
        union(a, b)
        total_cost += cost
        mx_time = max(mx_time, time)

one = find(1)
print(*(mx_time, total_cost) if all(find(node) == one for node in range(2, n+1)) else (-1,))