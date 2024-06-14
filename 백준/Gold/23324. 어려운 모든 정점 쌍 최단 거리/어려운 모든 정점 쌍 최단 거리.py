# https://www.acmicpc.net/problem/23324
import sys
input = sys.stdin.readline


def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    x = find(a)
    y = find(b)
    if x == y:
        return

    if rank[x] > rank[y]:
        parent[y] = x
        rank[x] += rank[y]
    else:
        parent[x] = y
        rank[y] += rank[x]


n, m, k = map(int, input().split())
parent, rank = list(range(n+1)), [1] * (n+1)
x, y = -1, -1
for i in range(1, m+1):
    u, v = map(int, input().split())
    if i == k:
        x, y = u, v
    else:
        union(u, v)

if find(x) == find(y):
    print(0)
else:
    groups = [find(node) for node in range(n+1)]
    x_group_cnt = groups.count(find(x))
    y_group_cnt = groups.count(find(y))
    print(x_group_cnt * y_group_cnt)