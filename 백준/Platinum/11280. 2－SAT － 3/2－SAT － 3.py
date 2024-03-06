# https://www.acmicpc.net/problem/11280
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
INF = int(1e5)


def get_strongly_connected_component(now):
    global order, possible
    visited[now] = order
    order += 1
    stack.append(now)

    group_first = visited[now]
    for nxt in graph[now]:
        nxt_group_first = visited[nxt] if visited[nxt] else get_strongly_connected_component(nxt)
        group_first = min(group_first, nxt_group_first)

    if visited[now] == group_first:
        group = set()
        while 1:
            top = stack.pop()
            if -top in group:
                possible = False

            group.add(top)
            visited[top] = INF
            if top == now:
                break

        scc.append(group)
    return group_first


n, m = map(int, input().split())
graph = [[] for _ in range(2*n+2)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[-a].append(b)
    graph[-b].append(a)

visited, order, stack = [0] * (2*n+2), 0, []
possible, scc = True, []
for start in range(1, n+1):
    if not visited[start]:
        get_strongly_connected_component(start)
    if not visited[-start]:
        get_strongly_connected_component(-start)

    if not possible:
        break

print(int(possible))