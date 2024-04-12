from copy import deepcopy
from collections import deque


def dfs_find_area(num, idx, L):
    if num==3:
        occur.append(L)
        return

    for i in range(idx, len(empty)):
        L.append(empty[i])
        dfs_find_area(num+1, i+1, deepcopy(L))
        L.pop()


def bfs(visited):
    Q = deque()
    for p, q in polluted_start:
        Q.appendleft([p, q])
        visited[p][q] = True
    polluted_count = 0

    while Q:
        x, y = Q.pop()
        if research[x][y] == 0:
            polluted_count += 1

        go = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        for nxt in go:
            pp, qq = x+nxt[0], y+nxt[1]
            if pp<0 or pp>=n or qq<0 or qq>=m:
                continue
            if visited[pp][qq]:
                continue
            if research[pp][qq]==1:
                continue
            visited[pp][qq] = True
            Q.appendleft([pp, qq])

    return polluted_count


n, m = map(int, input().split())
research = [list(map(int, input().split())) for _ in range(n)]
clean_count = 0
polluted_start = []
for i in range(n):
    for j in range(m):
        if research[i][j] == 0 :
            clean_count += 1
        if research[i][j] == 2:
            polluted_start.append([i, j])

empty = []
for i in range(n):
    for j in range(m):
        if research[i][j] == 0:
            empty.append([i, j])

occur = []
dfs_find_area(0, 0, [])

max_safe = 0

for area in occur:
    for a, b in area:
        research[a][b] = 1

    visited = [[False]*m for _ in range(n)]

    now = clean_count - bfs(visited)
    max_safe = max(max_safe, now-3)

    for a, b in area:
        research[a][b] = 0

print(max_safe)