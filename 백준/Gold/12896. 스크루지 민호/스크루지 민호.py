# https://www.acmicpc.net/problem/12896
import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(2e5))


def dfs(now, bef):
    max_depth, max_node = 0, now
    for nxt in graph[now]:
        if nxt == bef:
            continue

        nxt_max_depth, nxt_max_node = dfs(nxt, now)
        if max_depth < nxt_max_depth + 1:
            max_depth = nxt_max_depth + 1
            max_node = nxt_max_node

    return max_depth, max_node


n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

_, one = dfs(1, 0)
dist, _ = dfs(one, 0)
print(dist + 1 >> 1)