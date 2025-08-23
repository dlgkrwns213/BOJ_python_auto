# https://www.acmicpc.net/problem/6951
import sys
input = sys.stdin.readline
INF = float('inf')

n, w, p = map(int, input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(n+1):
    graph[i][i] = 0
    
for _ in range(w):
    u, v, w = map(int, input().split())
    graph[u][v] = w
    graph[v][u] = w

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][k] != INF and graph[k][j] != INF:
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

print('\n'.join(map(lambda ipt: str(graph[ipt[0]][ipt[1]]), [list(map(int, input().split())) for _ in range(p)])))