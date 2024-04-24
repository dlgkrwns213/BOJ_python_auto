import sys
from collections import deque
input = sys.stdin.readline


def dfs(pre, now):
    visited[now] = True
    line[now] = 0
    for nxt in subway[now]:
        if nxt == pre or visited[nxt]:
            continue

        line[nxt] -= 1
        if line[nxt] == 1:
            dfs(now, nxt)


def bfs(start):
    q = deque()
    q.appendleft((start, 0))
    visited[start] = True

    while q:
        now, cnt = q.pop()
        for nxt in subway[now]:
            if distance[nxt] != -1:
                continue

            q.appendleft((nxt, cnt+1))
            distance[nxt] = cnt+1


n = int(input())
subway, line = [[] for _ in range(n+1)], [0]*(n+1)

for _ in range(n):
    a, b = map(int, input().split())
    subway[a].append(b)
    subway[b].append(a)
    line[a] += 1
    line[b] += 1

visited = [False] * (n+1)
for i, v in enumerate(line):
    if v == 1:
        dfs(-1, i)

distance = [-1] * (n+1)
for i, x in enumerate(line):
    if x == 2:
        distance[i] = 0
for i, x in enumerate(line):
    if x:
        distance[i] = 0
        bfs(i)

print(*distance[1:])
