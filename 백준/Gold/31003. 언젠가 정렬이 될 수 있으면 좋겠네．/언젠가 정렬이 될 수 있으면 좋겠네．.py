# https://www.acmicpc.net/problem/31003
from math import gcd
from heapq import heappush, heappop


def topological_sort():
    hq = []
    for idx, cnt in enumerate(counts):
        if not cnt:
            heappush(hq, (a[idx], idx))

    ans = []
    while hq:
        now, now_idx = heappop(hq)
        ans.append(now)

        for nxt_idx in graph[now_idx]:
            counts[nxt_idx] -= 1
            if not counts[nxt_idx]:
                heappush(hq, (a[nxt_idx], nxt_idx))

    return ans


n = int(input())
a = list(map(int, input().split()))

graph, counts = [[] for _ in range(n)], [0] * n
for i, front in enumerate(a):
    for j, back in enumerate(a[i+1:], i+1):
        if gcd(front, back) > 1:
            graph[i].append(j)
            counts[j] += 1

print(' '.join(map(str, topological_sort())))