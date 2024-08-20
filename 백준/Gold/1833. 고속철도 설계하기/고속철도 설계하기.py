# https://www.acmicpc.net/problem/1833
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
costs, total = [], 0
parent, rank = list(range(n)), [1] * n
for i in range(n):
    for j, v in enumerate(map(int, input().split())):
        if i >= j:
            continue

        if v < 0:
            total += -v
            if find(i) != find(j):
                union(i, j)
        else:
            costs.append((v, i, j))
costs.sort(key=lambda cost: cost[0])

builds = []
for w, a, b in costs:
    if find(a) != find(b):
        union(a, b)
        total += w
        builds.append((a+1, b+1))

print(total, len(builds))
print('\n'.join(map(lambda build: ' '.join(map(str, build)), builds)))