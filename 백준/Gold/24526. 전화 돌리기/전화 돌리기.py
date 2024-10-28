# https://www.acmicpc.net/problem/24526
import sys
input = sys.stdin.readline


def topological_sort():
    stack = [i for i, cnt in enumerate(counts[1:], 1) if not cnt]

    ans = 0
    while stack:
        now = stack.pop()
        ans += 1
        for nxt in graph[now]:
            counts[nxt] -= 1
            if not counts[nxt]:
                stack.append(nxt)
    return ans


n, m = map(int, input().split())
graph, counts = [[] for _ in range(n+1)], [0] * (n+1)
for _ in range(m):
    u, v = map(int, input().split())
    graph[v].append(u)
    counts[u] += 1

print(topological_sort())