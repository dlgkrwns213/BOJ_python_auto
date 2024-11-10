# https://www.acmicpc.net/problem/2572
import sys
input = sys.stdin.readline


n = int(input())
route = ''.join(input().split())
m, k = map(int, input().split())
graph: list[list[tuple]] = [[] for _ in range(m+1)]
for _ in range(k):
    u, v, c = input().split()
    u, v = map(int, (u, v))
    graph[u].append((v, c))
    graph[v].append((u, c))

dp = [[0]*(m+1) for _ in range(n+1)]
for i in range(n-1, -1, -1):
    want_color = route[i]
    for now in range(m, 0, -1):
        ret = 0
        for nxt, color in graph[now]:
            ret = max(ret, dp[i+1][nxt] + (10 if color == want_color else 0))
        dp[i][now] = ret
print(dp[0][1])
