# https://www.acmicpc.net/problem/17839
import sys
from collections import deque
input = sys.stdin.readline


def bfs(start):
    if start == -1:
        return set()

    q = deque()
    q.append(start)

    visited = [0] * len(idxs)
    visited[start] = 1

    ret = set()
    while q:
        now = q.popleft()

        for nxt in graph[now]:
            if visited[nxt]:
                continue

            visited[nxt] = 1
            ret.add(nxt)
            q.append(nxt)

    return ret


graph: list[list] = []
idxs: dict = {}
for _ in range(int(input())):
    p, _, q = input().split()
    if p not in idxs:
        idxs[p] = len(idxs)
        graph.append([])
    if q not in idxs:
        idxs[q] = len(idxs)
        graph.append([])

    graph[idxs[p]].append(idxs[q])

can_idxs = bfs(idxs.get('Baba', -1))
print('\n'.join(sorted(name for name in idxs if idxs[name] in can_idxs)))