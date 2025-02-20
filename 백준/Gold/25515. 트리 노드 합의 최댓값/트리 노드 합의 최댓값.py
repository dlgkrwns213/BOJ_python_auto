# https://www.acmicpc.net/problem/25515
import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e5)+9)


def dfs(now):
    ret = weights[now]
    for child in graph[now]:
        ret += dfs(child)

    return max(ret, 0)


n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n-1):
    p, c = map(int, input().split())
    graph[p].append(c)
weights = list(map(int, input().split()))

ans = weights[0]
for nc in graph[0]:
    ans += dfs(nc)
print(ans)