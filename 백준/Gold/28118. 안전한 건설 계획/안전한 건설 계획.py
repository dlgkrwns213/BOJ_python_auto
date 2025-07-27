# https://www.acmicpc.net/problem/28118
import sys
input = sys.stdin.readline


def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x, y = map(find, (x, y))

    if x == y:
        return

    if rank[x] >= rank[y]:
        parent[y] = x
        rank[x] += rank[y]
    else:
        parent[x] = y
        rank[y] += rank[x]


n, m = map(int, input().split())
parent = list(range(n+1))
rank = [1] * (n+1)
for _ in range(m):
    union(*map(int, input().split()))

cnt = 0
for i in range(1, n):
    if find(i) != find(i+1):
        union(i, i+1)
        cnt += 1

print(cnt)