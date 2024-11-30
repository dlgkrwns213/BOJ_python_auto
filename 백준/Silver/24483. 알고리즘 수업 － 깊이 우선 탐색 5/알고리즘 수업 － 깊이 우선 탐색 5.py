import sys
sys.setrecursionlimit(int(3e6))
input = sys.stdin.readline


def dfs(now):
    global order
    orders[now] = order
    for nxt in graph[now]:
        if visited[nxt] == -1:
            visited[nxt] = visited[now] + 1
            order += 1
            dfs(nxt)


n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for line in graph:
    line.sort()

visited, orders = [-1] * (n+1), [0] * (n+1)
visited[r], order = 0, 1
dfs(r)

print(sum(map(lambda idx: visited[idx]*orders[idx], range(n+1))))