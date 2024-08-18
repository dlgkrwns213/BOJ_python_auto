# https://www.acmicpc.net/problem/6091
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


n = int(input())
distances = [(v, i, i+j+1) for i in range(n-1) for j, v in enumerate(map(int, input().split()))]
distances.sort()

parent, rank, graph = list(range(n)), [1] * n, [[] for _ in range(n)]
for d, a, b in distances:
    if find(a) != find(b):
        union(a, b)
        graph[a].append(b+1)
        graph[b].append(a+1)

ans = []
for line in graph:
    ans.append(f'{len(line)} {" ".join(map(str, sorted(line)))}')
print('\n'.join(ans))