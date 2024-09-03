# https://www.acmicpc.net/problem/16393
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
distances = []
for i in range(n):
    for j, v in enumerate(map(int, input().split()[:i])):
        distances.append((j, i, v))
distances.sort(key=lambda distance: distance[2])

parent, rank = list(range(n)), [1] * n
links = []
for i, j, v in distances:
    if find(i) != find(j):
        union(i, j)
        links.append((i+1, j+1))

print('\n'.join(map(lambda line: ' '.join(map(str, line)), links)))