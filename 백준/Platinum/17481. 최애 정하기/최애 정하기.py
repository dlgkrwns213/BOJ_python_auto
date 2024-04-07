# https://www.acmicpc.net/problem/17481
import sys
input = sys.stdin.readline


def dfs(now):
    if visited[now]:
        return False
    visited[now] = True

    for member in graph[now]:
        if matched[member] == -1:
            matched[member] = now
            return True
    for member in graph[now]:
        if dfs(matched[member]):
            matched[member] = now
            return True
    return False


n, m = map(int, input().split())
member_idx = {input().rstrip(): i for i in range(m)}

graph = [tuple(map(lambda member: member_idx[member], input().split()[1:])) for _ in range(n)]

matched = [-1] * m
for p in range(n):
    visited = [False] * n
    dfs(p)

matching = m - matched.count(-1)
print('YES' if matching == n else f'NO\n{matching}')