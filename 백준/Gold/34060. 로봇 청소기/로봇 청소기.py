# https://www.acmicpc.net/problem/34060
import sys
sys.setrecursionlimit(int(2e5))
input = sys.stdin.readline


def dfs(now):
    visited[now] = True
    for nxt in graph[now]:
        if not visited[nxt]:
            dfs(nxt)


n = int(input())
graph = [[] for _ in range(n)]
bef, now, last = dict(), dict(), -1
for idx in range(n):
    y = int(input())
    if y <= last:
        bef = now
        now = dict()
    elif y == last+1:
        graph[idx-1].append(idx)
        graph[idx].append(idx-1)

    last = y
    now[y] = idx

    if y in bef:
        bef_idx = bef[y]
        graph[bef_idx].append(idx)
        graph[idx].append(bef_idx)

count = 0
visited = [False] * n
for start in range(n):
    if not visited[start]:
        dfs(start)
        count += 1

print(f'{count}\n{n}')