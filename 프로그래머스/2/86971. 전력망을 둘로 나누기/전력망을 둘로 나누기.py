def solution(n, wires):
    graph = [[] for _ in range(n+1)]
    for u, v in wires:
        graph[u].append(v)
        graph[v].append(u)
        
    counts = [0] * (n+1)
    dfs(graph, counts, 1, 0)
    
    return min(map(lambda idx: abs(n-2*counts[idx]), range(1, n+1)))
        
        
def dfs(graph, counts, now, bef):
    ret = 1
    for nxt in graph[now]:
        if nxt == bef:
            continue
            
        ret += dfs(graph, counts, nxt, now)
        
    counts[now] = ret;
    return ret
        