# https://www.acmicpc.net/problem/8012
import sys
from math import ceil, log2
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline


def set_parent(now, dep=0):
    depth[now] = dep

    for nxt in graph[now]:
        if depth[nxt] == -1:
            ancestors[nxt][0] = now
            set_parent(nxt, dep+1)


def set_ancestor():
    set_parent(1, 0)

    for i in range(1, size):
        for j in range(1, n+1):
            ancestors[j][i] = ancestors[ancestors[j][i-1]][i-1]


def lca(x, y):
    if depth[x] > depth[y]:
        x, y = y, x

    dx = depth[x]
    dy = depth[y]
    for i in range(size-1, -1, -1):
        if depth[y] - depth[x] >= 1 << i:
            y = ancestors[y][i]

    if x == y:
        return dy - dx

    for i in range(size-1, -1, -1):
        if ancestors[x][i] != ancestors[y][i]:
            x = ancestors[x][i]
            y = ancestors[y][i]

    common = ancestors[x][0]
    return dx + dy - 2 * depth[common]


n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

size = ceil(log2(n))
ancestors = [[0]*size for _ in range(n+1)]
depth = [-1] * (n+1)

set_ancestor()

total = 0
bef = 1
for _ in range(int(input())):
    now = int(input())
    total += lca(bef, now)
    bef = now

print(total)