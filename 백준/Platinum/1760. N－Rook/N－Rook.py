# https://www.acmicpc.net/problem/1760
import sys
input = sys.stdin.readline


def get_graph():
    rows, row_idx, use = [[-1] * m for _ in range(n)], 0, False
    for i in range(n):
        for j in range(m):
            if board[i][j] in (0, 1):
                use = True
                rows[i][j] = row_idx
            elif board[i][j] == 2:
                if use:
                    row_idx += 1

        if use:
            row_idx += 1
            use = False

    cols, col_idx, use = [[-1] * m for _ in range(n)], 0, False
    for j in range(m):
        for i in range(n):
            if board[i][j] in (0, 1):
                use = True
                cols[i][j] = col_idx
            elif board[i][j] == 2:
                if use:
                    col_idx += 1

        if use:
            col_idx += 1
            use = False

    graph = [set() for _ in range(row_idx)]
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                graph[rows[i][j]].add(cols[i][j])

    return row_idx, col_idx, graph


def dfs(r):
    if visited[r]:
        return False
    visited[r] = True

    for c in graph[r]:
        if matched[c] == -1:
            matched[c] = r
            return True
    for c in graph[r]:
        if dfs(matched[c]):
            matched[c] = r
            return True

    return False


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

row, col, graph = get_graph()

matched = [-1] * col
for r in range(row):
    visited = [False] * row
    dfs(r)

print(col - matched.count(-1))
