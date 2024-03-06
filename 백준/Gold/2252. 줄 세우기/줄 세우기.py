# https://www.acmicpc.net/problem/2252
import sys
from heapq import heappop, heappush
input = sys.stdin.readline


def topological_sort():
    hq = []
    for i in range(1, n+1):
        if cnt[i] == 0:
            heappush(hq, i)

    ans = []
    for _ in range(n):
        now = heappop(hq)
        ans.append(now)
        for nxt in graph[now]:
            cnt[nxt] -= 1
            if cnt[nxt] == 0:
                heappush(hq, nxt)

    print(' '.join(map(str, ans)))


n, m = map(int, input().split())
graph, cnt = [[] for _ in range(n+1)], [0]*(n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    cnt[b] += 1

topological_sort()