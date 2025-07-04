from heapq import heappop, heappush
INF = float('inf')


def dijkstra(n, graph, gates, summit_sets):
    distances = [INF] * (n+1)
    hq = []
    
    for gate in gates:
        distances[gate] = 0
        heappush(hq, (0, gate))
        
    while hq:
        dist, now = heappop(hq)
        
        if now in summit_sets or distances[now] < dist:
            continue
            
        for nxt, nw in graph[now]:
            nxt_dist = max(dist, nw)
            if distances[nxt] > nxt_dist:
                distances[nxt] = nxt_dist
                heappush(hq, (nxt_dist, nxt))
                
    return distances
    
    

def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n+1)]
    for u, v, w in paths:
        graph[u].append((v, w))
        graph[v].append((u, w))
        
    distances = dijkstra(n, graph, gates, set(summits))
    answer_node = -1
    answer_val = INF

    for e in sorted(summits):
        if distances[e] < answer_val:
            answer_node = e
            answer_val = distances[e]

    return [answer_node, answer_val]
    