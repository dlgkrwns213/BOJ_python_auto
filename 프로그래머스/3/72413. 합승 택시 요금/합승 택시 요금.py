from heapq import heappop, heappush


def dijkstra(graph, n, start):
    INF = int(1e9)
    
    distances = [INF] * (n+1)
    distances[start] = 0
    
    hq = []
    heappush(hq, (0, start))
    
    while hq:
        dist, now = heappop(hq)
        
        if distances[now] < dist:
            continue
            
        for nxt, nd in graph[now]:
            nxt_dist = nd + dist
            
            if distances[nxt] > nxt_dist:
                distances[nxt] = nxt_dist
                heappush(hq, (nxt_dist, nxt))
                
    return distances


def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n+1)]
    for u, v, w in fares:
        graph[u].append((v, w))
        graph[v].append((u, w))
        
    distances_s = dijkstra(graph, n, s)
    distances_a = dijkstra(graph, n, a)
    distances_b = dijkstra(graph, n, b)
    
    return min(map(lambda idx: distances_s[idx] + distances_a[idx] + distances_b[idx], range(n+1)))