import sys
from collections import deque
input = sys.stdin.readline


def bfs(start):
    q = deque()
    q.append(start)

    depths = [-1] * (n+1)
    depths[start] = 0

    while q:
        now = q.popleft()
        for nxt in graph[now]:
            if depths[nxt] == -1:
                depths[nxt] = depths[now] + 1
                q.append(nxt)

    return depths


n = int(input())
graph, root = [[] for _ in range(n+1)], -1
for idx in range(1, n+1):
    parent = int(input())
    if parent == -1:
        root = idx
    else:
        graph[parent].append(idx)

print('\n'.join(map(str, bfs(root)[1:])))