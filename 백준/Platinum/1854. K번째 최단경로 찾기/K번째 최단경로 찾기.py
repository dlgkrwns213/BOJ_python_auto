import sys
from heapq import heappop, heappush
input = sys.stdin.readline
print = sys.stdout.write
INF = 10**9


def dijkstra(start):
    distances = [[] for _ in range(n+1)]  # max_heap
    distances[start].append(0)
    counts = [0] * (n+1)
    q = [(0, start)]
    
    while q:
        dist, now = heappop(q)
        
        for nt, nxt in graph[now]:
            nxt_dist = nt + dist
            if len(distances[nxt]) < k:
                heappush(distances[nxt], -nxt_dist)
                heappush(q, (nxt_dist, nxt))
            elif -1*distances[nxt][0] > nxt_dist:
                heappop(distances[nxt])
                heappush(distances[nxt], -nxt_dist)
                heappush(q, (nxt_dist, nxt))

    return distances[1:]
            
            
n, m, k = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

ans = dijkstra(1)
for line in ans:
    if len(line) < k:
        print('-1\n')
    else:
        ans = sorted(map(lambda x: -x, line))
        print(str(ans[k-1]))
        print('\n')
