# https://www.acmicpc.net/problem/18231
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

k = int(input())
destroys = list(map(int, input().split()))
destroys_set = set(destroys)

possibles = []
for destroy in destroys:
    if all(near in destroys_set for near in graph[destroy]):
        possibles.append(destroy)

real = set()
for possible in possibles:
    real.add(possible)
    real.update(graph[possible])

if len(real) == len(destroys):
    print(len(possibles))
    print(' '.join(map(str, possibles)))
else:
    print(-1)