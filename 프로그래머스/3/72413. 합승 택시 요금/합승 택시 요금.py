from heapq import heappop, heappush
INF = int(1e9)


def solution(n, s, a, b, fares):
    def dijkstra(start):
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
        
        
    
    graph = [[] for _ in range(n+1)]
    for u, v, w in fares:
        graph[u].append((v, w))
        graph[v].append((u, w))
        
    s_distances = dijkstra(s)
    a_distances = dijkstra(a)
    b_distances = dijkstra(b)

    answer = min(map(lambda x: s_distances[x] + a_distances[x] + b_distances[x], range(1, n+1)))
    return answer