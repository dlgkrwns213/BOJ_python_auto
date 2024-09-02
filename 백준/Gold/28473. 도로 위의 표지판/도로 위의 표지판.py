# https://www.acmicpc.net/problem/28473
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
roads = [list(map(int, input().split())) for _ in range(m)]
roads.sort(key=lambda road: (road[2], road[3]))

parent, rank = list(range(n+1)), [1] * (n+1)
write, total = [], 0
for x, y, z, w in roads:
    if find(x) != find(y):
        union(x, y)
        write.append(z)
        total += w

one = find(1)
print(*(''.join(map(str, write)), total) if all(find(node) == one for node in range(2, n+1)) else (-1,))