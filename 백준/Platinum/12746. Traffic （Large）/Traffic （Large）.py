# https://www.acmicpc.net/problem/12745
import sys
from math import ceil, log2
sys.setrecursionlimit(int(1e7))
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

    for i in range(size-1, -1, -1):
        if depth[y] - depth[x] >= 1 << i:
            y = ancestors[y][i]

    if x == y:
        return x

    for i in range(size-1, -1, -1):
        if ancestors[x][i] != ancestors[y][i]:
            x = ancestors[x][i]
            y = ancestors[y][i]

    return ancestors[x][0]


def dfs(bef, now):
    ret = count[now]
    for nxt in graph[now]:
        if bef != nxt:
            ret += dfs(now, nxt)

    count[now] = ret
    return ret


n, q = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

size = ceil(log2(n))
ancestors = [[0]*size for _ in range(n+1)]
depth = [-1] * (n+1)

set_ancestor()

count = [0] * (n + 1)
for _ in range(q):
    c, d = map(int, input().split())
    count[c] += 1
    count[d] += 1
    count[lca(c, d)] -= 2
dfs(0, 1)

a, b = 0, 1
ans = 0
for i in range(2, n):
    if ans < count[i]:
        ans = count[i]
        a, b = ancestors[i][0], i
    elif ans == count[i]:
        j = ancestors[i][0]
        if i < a or j < b:
            a, b = i, j

a, b = min(a, b), max(a, b)
print(a, b, ans)