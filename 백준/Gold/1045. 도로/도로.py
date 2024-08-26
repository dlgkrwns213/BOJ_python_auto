# https://www.acmicpc.net/problem/1045
import sys
input = sys.stdin.readline


def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    counts[x] += 1
    counts[y] += 1
    x, y = map(find, (x, y))

    if rank[x] >= rank[y]:
        rank[x] += rank[y]
        parent[y] = x
    else:
        rank[y] += rank[x]
        parent[x] = y


n, m = map(int, input().split())
roads = []
for i in range(n):
    for j, v in enumerate(input().rstrip()[i+1:], i+1):
        if v == 'Y':
            roads.append((i, j))

parent, rank = list(range(n)), [1] * n
counts, use = [0] * n, [0] * len(roads)
for idx, road in enumerate(roads):
    a, b = road
    if find(a) != find(b):
        union(a, b)
        use[idx] = 1

if len(roads) < m:
    print(-1)
else:
    m -= n-1
    ri = 0
    while m:
        if not use[ri]:
            union(*roads[ri])
            m -= 1
        ri += 1

    zero = find(0)
    print(' '.join(map(str, counts)) if all(find(node) == zero for node in range(n)) else -1)