import sys
input = sys.stdin.readline
INF = int(1e6)

n, m = map(int, input().split())
graph = [set() for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

counts = [len(friends) for friends in graph]
mn = INF
for x in range(1, n+1):
    for y in graph[x]:
        if x < y:
            continue
        for z in graph[x]:
            if y > z and z in graph[y] and y in graph[z]:
                mn = min(mn, counts[x] + counts[y] + counts[z])

print(mn-6 if mn != INF else -1)