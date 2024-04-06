# https://www.acmicpc.net/problem/1348
import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')


# bfs
def get_distance(si: int, sj: int) -> list[int or INF]:
    go = ((-1, 0), (1, 0), (0, -1), (0, 1))

    q = deque()
    q.append((si, sj, 0))

    visited = [[False]*c for _ in range(r)]
    visited[si][sj] = True

    distances = [INF] * park_count
    while q:
        x, y, cnt = q.popleft()
        if (x, y) in park_idx:
            distances[park_idx[(x, y)]] = cnt

        for a, b in go:
            nx, ny = x + a, y + b
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            if board[nx][ny] == 'X' or visited[nx][ny]:
                continue

            visited[nx][ny] = True
            q.append((nx, ny, cnt+1))

    return distances


def get_graph() -> (int, list[list]):
    graph: list[list] = []
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'C':
                graph.append(get_distance(i, j))
    return len(graph), graph


# bipartite matching
def dfs(car: int, visited: list[bool], matched: list[int], parks: list[list[int]]):
    if visited[car]:
        return False
    visited[car] = True

    for park in parks[car]:
        if matched[park] == -1:
            matched[park] = car
            return True
    for park in parks[car]:
        if dfs(matched[park], visited, matched, parks):
            matched[park] = car
            return True

    return False


def get_bipartite_matching(mx_distance: int, cc: int, pc: int, graph: list[list]) -> bool:
    parks = [[pi for pi, pv in enumerate(graph[ci]) if pv <= mx_distance] for ci in range(cc)]

    matched = [-1] * pc
    for car in range(cc):
        visited = [False] * cc
        dfs(car, visited, matched, parks)
    return pc - matched.count(-1) >= cc


# binary search
def get_min_distance(cc: int, pc: int, graph: list[list]):
    if cc > pc:
        return -1

    left, right = 0, r*c
    while left < right:
        mid = left + right >> 1
        possible = get_bipartite_matching(mid, cc, pc, graph)
        if possible:
            right = mid
        else:
            left = mid + 1

    return left if left < r * c else -1


r, c = map(int, input().split())
board = [input().rstrip() for _ in range(r)]

park_idx, park_count = dict(), 0
for i in range(r):
    for j in range(c):
        if board[i][j] == 'P':
            park_idx[(i, j)] = park_count
            park_count += 1

car_count, graph = get_graph()
print(get_min_distance(car_count, park_count, graph))