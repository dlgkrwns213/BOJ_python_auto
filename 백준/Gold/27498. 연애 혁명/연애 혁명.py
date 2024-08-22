# https://www.acmicpc.net/problem/27498
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
parent, rank, relations, total = list(range(n+1)), [1] * (n+1), [], 0
for _ in range(m):
    a, b, c, d = map(int, input().split())
    if d:
        union(a, b)
    else:
        total += c
        relations.append((c, a, b))
relations.sort(key=lambda relation: -relation[0])

for c, a, b in relations:
    if find(a) != find(b):
        union(a, b)
        total -= c

print(total)