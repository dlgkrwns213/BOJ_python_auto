def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    fx, fy = map(find, (x, y))

    if fx < fy:
        parent[fx] = fy
    else:
        parent[fy] = fx


n, m, q = map(int, input().split())
parent = list(range(n+1))

for _ in range(m):
    union(*map(int, input().split()))

ans = []
for _ in range(q):
    u, v = map(int, input().split())
    ans.append('Y' if find(u) == find(v) else 'N')
print('\n'.join(ans))