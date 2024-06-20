# https://www.acmicpc.net/problem/19581
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline


def dfs1(now, bef):
    mx_dist, mx_node = 0, now
    for nxt, weight in graph[now]:
        if nxt == bef:
            continue

        nxt_dist, nxt_node = dfs1(nxt, now)
        if mx_dist < nxt_dist + weight:
            mx_dist = nxt_dist + weight
            mx_node = nxt_node

    return mx_dist, mx_node


def dfs2(now, visited, dist):
    visited[now] = dist

    for nxt, weight in graph[now]:
        if visited[nxt] != -1:
            continue
        dfs2(nxt, visited, dist + weight)


n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

_, x = dfs1(1, 0)

x_visited = [-1] * (n+1)
dfs2(x, x_visited, 0)
y = x_visited.index(max(x_visited))

y_visited = [-1] * (n+1)
dfs2(y, y_visited, 0)

x_max = max([v for i, v in enumerate(x_visited) if i != y])
y_max = max([v for i, v in enumerate(y_visited) if i != x])
print(max(x_max, y_max))