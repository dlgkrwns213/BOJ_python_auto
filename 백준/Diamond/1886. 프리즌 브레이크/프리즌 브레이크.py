# https://www.acmicpc.net/problem/1886
import sys
from collections import deque
input = sys.stdin.readline


def bfs(dx, dy, start_idx):
    go = ((-1, 0), (1, 0), (0, -1), (0, 1))

    q = deque()
    q.append((dx, dy, 0))
    visited = [[True if board[i][j] != '.' else False for j in range(m)] for i in range(n)]

    distances = dict()
    while q:
        x, y, cnt = q.popleft()

        for a, b in go:
            nx, ny = x + a, y + b
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited[nx][ny]:
                continue

            visited[nx][ny] = True
            distances[start_idx[(nx, ny)]] = cnt + 1
            q.append((nx, ny, cnt + 1))

    return distances


def get_graph() -> (int, int, list[dict]):
    start_idx, si = {}, 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == '.':
                start_idx[(i, j)] = si
                si += 1

    graph = []
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'D':
                graph.append(bfs(i, j, start_idx))

    possible = {value for line in graph for value in line}
    if len(possible) != si:
        return -1, -1, graph

    return si, len(graph), graph


def dfs(destination, visited, matched, can_go_graph):
    if visited[destination]:
        return False
    visited[destination] = True

    for start in can_go_graph[destination]:
        if matched[start] == -1:
            matched[start] = destination
            return True
    for start in can_go_graph[destination]:
        if dfs(matched[start], visited, matched, can_go_graph):
            matched[start] = destination
            return True
    return False


def is_possible(time):
    can_go_graph: list[list] = [[] for _ in graph]
    for destination, line in enumerate(graph):
        for start in line:
            if line[start] <= time:
                can_go_graph[destination].append(start)

    # 탈출구 -> 현재 위치가 가능한지?
    matched = [-1] * start_count
    for destination in range(destination_count):
        for _ in range(time):  # 시간 만큼 탈출 가능 (나가는 시간 >= 거리)
            visited = [False] * destination_count
            dfs(destination, visited, matched, can_go_graph)

    return False if -1 in matched else True


n, m = map(int, input().split())
board = [input().rstrip() for _ in range(n)]

start_count, destination_count, graph = get_graph()
if start_count == -1:
    print('impossible')
else:
    left, right = 0, n*m
    while left < right:
        mid = left + right >> 1
        if is_possible(mid):
            right = mid
        else:
            left = mid + 1

    print(left)