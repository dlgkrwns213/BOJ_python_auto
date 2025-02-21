# https://www.acmicpc.net/problem/1289
import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e5)+9)
MOD = int(1e9+7)


def dfs(node, parent):
    global total
    weight = 1
    for child, w in graph[node]:
        if child == parent:
            continue

        nxt_weight = dfs(child, node)
        total += weight * nxt_weight * w
        weight += nxt_weight * w

    return weight


n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))

total = 0
dfs(1, 0)
print(total % MOD)