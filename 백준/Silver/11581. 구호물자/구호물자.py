import sys
input = sys.stdin.readline


def is_cycle(now):
    if visited[now] == 1:
        return True
    if visited[now] == 2:
        return False

    visited[now] = 1
    for nxt in graph[now]:
        if is_cycle(nxt):
            return True
    visited[now] = 2
    return False


n = int(input())
graph = [[] for _ in range(n+1)]
for i in range(1, n):
    input()
    for c in map(int, input().split()):
        graph[i].append(c)

visited = [0] * (n+1)
print(f'{"" if is_cycle(1) else "NO "}CYCLE')