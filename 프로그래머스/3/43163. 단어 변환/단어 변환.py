from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    words.append(begin)
    idx = len(words[0])
    n = len(words)
    graph = [[] for _ in range(n)]
    for i, wi in enumerate(words):
        for j, wj in enumerate(words[:i]):
            if sum(map(lambda i: 1 if wi[i] != wj[i] else 0, range(idx))) == 1:
                graph[i].append(j)
                graph[j].append(i)
                
    return bfs(graph, n, n-1, words.index(target))
    

def bfs(graph, n, start, destination):
    visited = [0] * n
    visited[start] = 1
    
    q = deque()
    q.append((start, 0))
    
    while q:
        now, count = q.popleft()
        if now == destination:
            return count
        
        for nxt in graph[now]:
            if not visited[nxt]:
                visited[nxt] = 1
                q.append((nxt, count+1))
                
    return 0            
    