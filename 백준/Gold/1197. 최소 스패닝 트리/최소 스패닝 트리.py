import sys
input = sys.stdin.readline


def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return

    if rank[x] > rank[y]:
        parent[y] = x
        rank[x] += rank[y]
    else:
        parent[x] = y
        rank[y] += rank[x]


v, e = map(int, input().split())
edge, parent, rank = [], list(range(v+1)), [1] * (v+1)
for _ in range(e):
    edge.append(tuple(map(int, input().split())))
edge.sort(key=lambda t: t[2])

total = 0
for a, b, w in edge:
    if find(a) != find(b):
        union(a, b)
        total += w
print(total)
