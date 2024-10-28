# https://www.acmicpc.net/problem/18780
import sys
from heapq import heappush, heappop
input = sys.stdin.readline


def topological_sort():
    hq, days = [], s.copy()
    for i, cnt in enumerate(counts[1:], 1):
        if not cnt:
            heappush(hq, (s[i], i))
            days[i] = s[i]

    while hq:
        now_day, now = heappop(hq)
        for nxt, gap in graph[now]:
            counts[nxt] -= 1
            days[nxt] = max(days[nxt], days[now]+gap)
            if not counts[nxt]:
                heappush(hq, (days[nxt], nxt))

    return days[1:]


n, m, c = map(int, input().split())
s = [0] + list(map(int, input().split()))
graph, counts = [[] for _ in range(n+1)], [0] * (n+1)
for _ in range(c):
    a, b, x = map(int, input().split())
    graph[a].append((b, x))
    counts[b] += 1

print('\n'.join(map(str, topological_sort())))