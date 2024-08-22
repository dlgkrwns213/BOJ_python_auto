# https://www.acmicpc.net/problem/1185
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


n, p = map(int, input().split())
costs = [0] + [int(input()) for _ in range(n)]
connections = []
for _ in range(p):
    s, e, l = map(int, input().split())
    connections.append((s, e, 2*l + costs[s] + costs[e]))

connections.sort(key=lambda connection: connection[2])

parent, rank, total = list(range(n+1)), [1] * (n+1), 0
for s, e, w in connections:
    if find(s) != find(e):
        union(s, e)
        total += w

print(total + min(costs[1:]))