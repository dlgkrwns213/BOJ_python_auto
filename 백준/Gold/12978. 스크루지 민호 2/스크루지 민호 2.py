# https://www.acmicpc.net/problem/12978
import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))


def dfs(now, parent):
    no, yes = 0, 1
    for child in graph[now]:
        if child == parent:
            continue

        dfs(child, now)
        no += dp[child][1]
        yes += min(dp[child])

    dp[now] = [no, yes]


n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dp = [[0]*2 for _ in range(n+1)]
dfs(1, -1)

print(min(dp[1]))