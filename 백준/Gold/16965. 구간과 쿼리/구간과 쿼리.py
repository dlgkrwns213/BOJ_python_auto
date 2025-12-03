import sys
from collections import deque
input = sys.stdin.readline


def bfs(start, dest):
    visited = [False] * len(graph)
    q = deque([start])
    visited[start] = True

    while q:
        cur = q.popleft()
        if cur == dest:
            return True

        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)

    return False


graph = []
intervals = []

for _ in range(int(input())):
    cmd, a, b = map(int, input().split())

    if cmd == 1:
        idx = len(intervals)
        intervals.append((a, b))
        graph.append([])

        # 비교는 항상 이전 구간들과만 (i < idx)
        for i in range(idx):
            x, y = intervals[i]

            # i -> idx 조건
            if a < x < b or a < y < b:
                graph[i].append(idx)

            # idx -> i 조건 (단, i < idx 이므로 가능)
            if x < a < y or x < b < y:
                graph[idx].append(i)

    else:
        print(1 if bfs(a-1, b-1) else 0)
