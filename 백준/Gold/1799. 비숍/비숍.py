# https://www.acmicpc.net/problem/2570
import sys
input = sys.stdin.readline


def get_graph(board):
    ups, up_idx, use = [[-1]*n for _ in range(n)], 0, False
    for i in range(n):
        for j in range(i+1):
            if board[i-j][j]:
                ups[i-j][j] = up_idx
                use = True
        if use:
            up_idx += 1
            use = False
    for i in range(1, n):
        for j in range(n-i):
            if board[n-1-j][i+j]:
                ups[n-1-j][i+j] = up_idx
                use = True
        if use:
            up_idx += 1
            use = False

    downs, down_idx, use = [[-1]*n for _ in range(n)], 0, False
    for i in range(n-1, -1, -1):
        for j in range(n-i):
            if board[i+j][j]:
                downs[i+j][j] = down_idx
                use = True
        if use:
            down_idx += 1
            use = False

    for i in range(1, n):
        for j in range(n-i):
            if board[j][i+j]:
                downs[j][i+j] = down_idx
                use = True
        if use:
            down_idx += 1
            use = False

    graph = [set() for _ in range(up_idx)]
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                graph[ups[i][j]].add(downs[i][j])

    return up_idx, down_idx, graph


def dfs(x):
    if visited[x]:
        return False
    visited[x] = True

    for y in graph[x]:
        if matched[y] == -1:
            matched[y] = x
            return True
    for y in graph[x]:
        if dfs(matched[y]):
            matched[y] = x
            return True
    return False


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

up, down, graph = get_graph(board)

matched = [-1] * down
for x in range(up):
    visited = [False] * up
    dfs(x)

print(down - matched.count(-1))
