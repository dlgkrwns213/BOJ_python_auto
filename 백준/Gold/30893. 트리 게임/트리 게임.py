# https://www.acmicpc.net/problem/30893
import sys
input = sys.stdin.readline


def get_route():
    stack = [s]

    log = [-1] * (n+1)
    log[s] = 0
    while stack:
        now = stack.pop()
        if now == e:
            break
        for nxt in graph[now]:
            if log[nxt] != -1:
                continue

            log[nxt] = now
            stack.append(nxt)

    now, route = e, [e]
    while now != s:
        now = log[now]
        route.append(now)

    return route[::-1]


n, s, e = map(int, input().split())
graph, counts = [[] for _ in range(n+1)], [0] * (n+1)
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

    counts[u] += 1
    counts[v] += 1

route = get_route()
print('First' if all(counts[node] <= 2 for node in route[1:-1:2]) else 'Second')