from collections import deque


def solution(begin, target, words):
    if target not in words:
        return 0
    words += [target, begin]
    n = len(words)
    size = len(words[0])
    
    graph = [[] for _ in range(n)]
    for i, vi in enumerate(words):
        for j, vj in enumerate(words[:i]):
            count = sum(map(lambda idx: 1 if vi[idx] != vj[idx] else 0, range(size)))
            if count == 1:
                graph[i].append(j)
                graph[j].append(i)
                
    print(graph)
    return bfs(graph, n)

    
def bfs(graph, n):
    visited = [False] * n
    visited[n-1] = True
    
    q = deque()
    q.append((n-1, 0))
    
    while q:
        now, count = q.popleft()
        if now == n-2:
            return count
        
        for nxt in graph[now]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append((nxt, count+1))
                
    return 0