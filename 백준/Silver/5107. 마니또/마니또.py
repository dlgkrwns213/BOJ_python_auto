import sys
input = sys.stdin.readline


def dfs(now):
    visited[now] = True
    for nxt in graph[now]:
        if not visited[nxt]:
            visited[nxt] = True
            dfs(nxt)


ans = []
for tc in range(1, int(1e6)):
    n = int(input())
    if not n:
        break

    name = dict()
    graph = [[] for _ in range(n)]
    for _ in range(n):
        a, b = input().split()
        if a not in name:
            name[a] = len(name)
        if b not in name:
            name[b] = len(name)

        graph[name[a]].append(name[b])

    visited = [0] * n
    cnt = 0
    for i in range(n):
        if not visited[i] and graph[i]:
            dfs(i)
            cnt += 1
    ans.append(f'{tc} {cnt}')

print('\n'.join(ans))