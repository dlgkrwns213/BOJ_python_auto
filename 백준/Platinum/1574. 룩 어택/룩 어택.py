# https://www.acmicpc.net/problem/1574
import sys
input = sys.stdin.readline


def get_graph():
    rows = [[-1]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if board[i][j]:
                rows[i][j] = i

    cols = [[-1]*c for _ in range(r)]
    for j in range(c):
        for i in range(r):
            if board[i][j]:
                cols[i][j] = j

    graph = [set() for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if board[i][j]:
                graph[rows[i][j]].add(cols[i][j])

    return graph


def dfs(row):
    if visited[row]:
        return False
    visited[row] = True

    for col in graph[row]:
        if matched[col] == -1:
            matched[col] = row
            return True
    for col in graph[row]:
        if dfs(matched[col]):
            matched[col] = row
            return True

    return False


r, c, n = map(int, input().split())
board = [[1]*c for _ in range(r)]
for _ in range(n):
    a, b = map(lambda x: int(x)-1, input().split())
    board[a][b] = 0

graph = get_graph()

matched = [-1] * c
for row in range(r):
    visited = [0] * r
    dfs(row)

print(c - matched.count(-1))