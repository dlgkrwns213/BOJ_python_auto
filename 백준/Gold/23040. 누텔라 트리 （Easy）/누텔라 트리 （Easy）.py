# https://www.acmicpc.net/problem/23040
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


n = int(input())
connects = [list(map(int, input().split())) for _ in range(n-1)]
colors = ' ' + input().rstrip()

parent, rank = list(range(n+1)), [1] * (n+1)
for u, v in connects:
    if colors[u] == 'R' and colors[v] == 'R':
        union(u, v)

graph = [set() for _ in range(n+1)]
for u, v in connects:
    cu, cv = colors[u], colors[v]
    if cu == 'B' and cv == 'R':
        graph[u].add(find(v))
    elif cv == 'B' and cu == 'R':
        graph[v].add(find(u))

print(sum(rank[near] for i in range(1, n+1) for near in graph[i]))