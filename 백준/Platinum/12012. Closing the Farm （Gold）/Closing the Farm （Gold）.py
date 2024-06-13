# https://www.acmicpc.net/problem/12012
import sys
input = sys.stdin.readline


def find(a):
    if parent[a] == a:
        return parent[a]
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


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

closing = [int(input()) for _ in range(n)]
opened = [0] * (n+1)
parent, rank = list(range(n+1)), [1] * (n+1)
ans = []
for idx, now in enumerate(closing[::-1]):
    opened[now] = 1
    for near in graph[now]:
        if opened[near]:
            union(now, near)

    ans.append(idx+1 == rank[find(now)])

print('\n'.join(map(lambda x: 'YES' if x else 'NO', ans[::-1])))