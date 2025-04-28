
import sys
input = sys.stdin.readline


def dfs(now):
    global order
    visited[now] = order
    order += 1

    stack.append(now)
    group_first = visited[now]
    for nxt in graph[now]:
        nxt_group_first = visited[nxt] if visited[nxt] else dfs(nxt)
        group_first = min(group_first, nxt_group_first)

    if group_first == visited[now]:
        group = []
        represents.add(now)
        while True:
            top = stack.pop()
            visited[top] = n + 1
            group.append(top)
            my_represent[top] = now
            if top == now:
                break

        scc.append(sorted(group))
    return group_first


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

visited, order, stack = [0] * (n+1), 1, []
scc, represents, my_represent = [], set(), list(range(n+1))
for start in range(1, n+1):
    if not visited[start]:
        dfs(start)

is_root = {represent: True for represent in represents}
for a, line in enumerate(graph):
    for b in line:
        ra, rb = my_represent[a], my_represent[b]
        if ra != rb:
            is_root[rb] = False

print(sum(is_root.values()))