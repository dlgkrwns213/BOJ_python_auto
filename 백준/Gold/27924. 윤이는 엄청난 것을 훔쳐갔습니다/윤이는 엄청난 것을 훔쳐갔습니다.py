# https://www.acmicpc.net/problem/27924
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = float('inf')


def dfs(now, bef, distances, depth=0):
    distances[now] = depth
    for nxt in graph[now]:
        if bef != nxt:
            dfs(nxt, now, distances, depth+1)


n = int(input())
graph = [[] for _ in range(n+1)]
counts = [0] * (n+1)
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

    counts[u] += 1
    counts[v] += 1
a, b, c = map(int, input().split())

leaves = [node for node in range(1, n+1) if counts[node] == 1]
distances_a = [INF] * (n+1)
distances_b = [INF] * (n+1)
distances_c = [INF] * (n+1)
dfs(a, 0, distances_a)
dfs(b, 0, distances_b)
dfs(c, 0, distances_c)

print('YES' if any(distances_a[node] < min(distances_b[node], distances_c[node]) for node in leaves) else 'NO')