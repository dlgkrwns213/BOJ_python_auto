# https://www.acmicpc.net/problem/9525
import sys
input = sys.stdin.readline


def get_graph():
    rows, row_idx, use = [[-1]*n for _ in range(n)], 0, False
    for i in range(n):
        for j in range(n):
            if board[i][j] == '.':
                rows[i][j] = row_idx
                use = True
            elif use:
                row_idx += 1
                use = False

        if use:
            row_idx += 1
            use = False

    cols, col_idx, use = [[-1] * n for _ in range(n)], 0, False
    for j in range(n):
        for i in range(n):
            if board[i][j] == '.':
                cols[i][j] = col_idx
                use = True
            elif use:
                col_idx += 1
                use = False

        if use:
            col_idx += 1
            use = False

    graph = [set() for _ in range(row_idx)]
    for i in range(n):
        for j in range(n):
            if board[i][j] == '.':
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


n = int(input())
board = [input().rstrip() for _ in range(n)]

row, col, graph = get_graph()

matched = [-1] * col
for r in range(row):
    visited = [False] * row
    dfs(r)

print(col - matched.count(-1))