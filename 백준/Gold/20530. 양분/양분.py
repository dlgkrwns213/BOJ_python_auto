# https://www.acmicpc.net/problem/20530
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


# dfs
def find_ancestors(now, ancestors):
    if not now:
        return

    ancestors.append(now)
    find_ancestors(parent[now], ancestors)


def dfs(now, p):
    visited[now] = 1
    for nxt in graph[now]:
        if nxt == p:
            continue

        if visited[nxt]:
            now_anc, nxt_anc = [], []
            find_ancestors(now, now_anc)
            find_ancestors(nxt, nxt_anc)

            mx, mn = now_anc, nxt_anc
            if len(mx) < len(mn):
                mx, mn = mn, mx
            for node in mx[:len(mx)-len(mn)+1]:
                is_cycled[node] = 1
        else:
            parent[nxt] = now
            dfs(nxt, now)


## dfs
def coloring(now):
    color[now] = node
    for nxt in graph[now]:
        if visited[nxt]:
            continue

        visited[nxt] = 1
        coloring(nxt)


n, q = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(n):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

is_cycled, visited = [0] * (n+1), [0] * (n+1)
parent = [-1] * (n + 1)
parent[1] = 0
dfs(1, 0)

color, visited = [-1] * (n+1), is_cycled.copy()
for node in range(1, n+1):
    if is_cycled[node]:
        coloring(node)

ans = []
for _ in range(q):
    u, v = map(int, input().split())
    ans.append(1 if color[u] == color[v] else 2)
print('\n'.join(map(str, ans)))