# https://www.acmicpc.net/problem/3865
import sys
from collections import defaultdict, deque
input = sys.stdin.readline


def bfs():
    q = deque()
    q.append(0)

    visited = [0] * len(name_idx)
    visited[0] = 1

    cnt = 0
    while q:
        now = q.popleft()
        if not graph[now]:
            cnt += 1
            continue

        for nxt in graph[now]:
            if visited[nxt]:
                continue

            visited[nxt] = 1
            q.append(nxt)

    return cnt


ans = []
while True:
    n = int(input())
    if not n:
        break

    name_idx, graph = dict(), defaultdict(list)
    for _ in range(n):
        front, rest = input().rstrip()[:-1].split(':')
        fi = name_idx.setdefault(front, len(name_idx))
        for back in rest.split(','):
            bi = name_idx.setdefault(back, len(name_idx))
            graph[fi].append(bi)

    ans.append(bfs())

print('\n'.join(map(str, ans)))