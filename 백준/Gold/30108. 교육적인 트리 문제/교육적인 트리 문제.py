# https://www.acmicpc.net/problem/30108
from heapq import heappop, heappush

n = int(input())
graph = [[] for _ in range(n+1)]
for c, p in enumerate(map(int, input().split()), 2):
    graph[p].append(c)
score = [0] + list(map(int, input().split()))

ans, total = [], 0
hq = [(-score[1], 1)]
for _ in range(n):
    max_score, node = heappop(hq)
    total -= max_score
    ans.append(total)

    for child in graph[node]:
        heappush(hq, (-score[child], child))

print('\n'.join(map(str, ans)))