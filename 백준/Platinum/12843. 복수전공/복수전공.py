# https://www.acmicpc.net/problem/12843
import sys
input = sys.stdin.readline


def dfs(now):
    if visited[now]:
        return False
    visited[now] = True

    for near in graph[now]:
        if matched[near] == -1:
            matched[near] = now
            return True
    for near in graph[now]:
        if dfs(matched[near]):
            matched[near] = now
            return True
    return False


n, m = map(int, input().split())
lectures = [''] * (n+1)
for _ in range(n):
    i, t = input().split()
    lectures[int(i)] = t

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    if lectures[a] == 'c':
        graph[a].append(b)
    else:
        graph[b].append(a)

matched = [-1] * (n+1)
for i in range(1, n+1):
    visited = [False] * (n+1)
    dfs(i)

print(matched.count(-1)-1)