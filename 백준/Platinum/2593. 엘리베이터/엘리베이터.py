# https://www.acmicpc.net/problem/2593
import sys
from collections import deque
input = sys.stdin.readline


def bfs(start, destination):
    q = deque()
    visited = [-2] * (m+1)

    destination_elevator = set()
    for elevator, ev in enumerate(elevators):
        x, y = ev
        if start >= x and not (start - x) % y:
            q.append((elevator, 1))
            visited[elevator] = -1
        if destination >= x and not (destination - x) % y:
            destination_elevator.add(elevator)

    while q:
        elevator, cnt = q.popleft()
        if elevator in destination_elevator:
            ans = []
            while elevator != -1:
                ans.append(elevator+1)
                elevator = visited[elevator]
            ans.append(cnt)
            return ans

        for nxt_elevator in graph[elevator]:
            if visited[nxt_elevator] != -2:
                continue

            visited[nxt_elevator] = elevator
            q.append((nxt_elevator, cnt+1))
    return (-1,)


n, m = map(int, input().split())
elevators = [list(map(int, input().split())) for _ in range(m)]
graph = [[] for _ in range(m)]
for i in range(m):
    for j in range(i+1, m):
        ix, iy = elevators[i]
        jx, jy = elevators[j]
        if ix > jx:
            ix, iy, jx, jy = jx, jy, ix, iy

        for floor in range(jx, n+1, jy):
            if not (floor - ix) % iy:
                graph[i].append(j)
                graph[j].append(i)
                break

a, b = map(int, input().split())
print('\n'.join(map(str, bfs(a, b)[::-1])))