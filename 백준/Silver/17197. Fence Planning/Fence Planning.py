def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x, y = map(find, (x, y))

    xd, xl, xu, xr = locations[x]
    yd, yl, yu, yr = locations[y]
    nxt = min(xd, yd), min(xl, yl), max(xu, yu), max(xr, yr)
    if rank[x] >= rank[y]:
        rank[x] += rank[y]
        parent[y] = x
        locations[x] = nxt
    else:
        rank[y] += rank[x]
        parent[x] = y
        locations[y] = nxt


n, m = map(int, input().split())
locations = [(0,)*4] + [tuple(map(int, input().split()))*2 for _ in range(n)]

parent, rank = list(range(n+1)), [1] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    if find(a) != find(b):
        union(a, b)

print(min(map(lambda idx: sum(locations[idx][2:])-sum(locations[idx][:2]) << 1 if parent[idx] == idx else float('inf'), range(1, n+1))))