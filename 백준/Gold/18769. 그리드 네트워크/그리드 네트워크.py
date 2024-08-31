# https://www.acmicpc.net/problem/18769
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


for _ in range(int(input())):
    r, c = map(int, input().split())

    costs = []
    for i in range(r):
        idx = c * i
        for v in map(int, input().split()):
            costs.append((idx, idx+1, v))
            idx += 1
    for i in range(r-1):
        idx = c * i
        for v in map(int, input().split()):
            costs.append((idx, idx+c, v))
            idx += 1

    costs.sort(key=lambda cost: cost[2])
    parent, rank, total = list(range(r*c)), [1] * (r*c), 0
    for x, y, cost in costs:
        if find(x) != find(y):
            union(x, y)
            total += cost

    print(total)