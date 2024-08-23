# https://www.acmicpc.net/problem/14574
import sys
from collections import deque
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


def bfs():
    q = deque()

    for node, line in enumerate(graph):
        if len(line) == 1:
            q.append((node, -1))
            break

    order = []
    while q:
        loser,  bef = q.popleft()
        for winner in graph[loser]:
            if winner == bef:
                continue

            order.append((loser+1, winner+1))
            q.append((winner, loser))

    return order[::-1]


n = int(input())
chefs = [list(map(int, input().split())) for _ in range(n)]
battles, bi = [0] * (n * (n-1) >> 1), 0
for i in range(n):
    pi, ci = chefs[i]
    for j in range(i+1, n):
        pj, cj = chefs[j]
        battles[bi] = (i, j, (ci+cj) // abs(pi-pj))
        bi += 1
battles.sort(key=lambda battle: -battle[2])

parent, rank, graph, total = list(range(n)), [1] * n, [[] for _ in range(n)], 0
for i, j, b in battles:
    if find(i) != find(j):
        union(i, j)
        graph[i].append(j)
        graph[j].append(i)
        total += b

print(total)
print('\n'.join(map(lambda line: ' '.join(map(str, line)), bfs())))