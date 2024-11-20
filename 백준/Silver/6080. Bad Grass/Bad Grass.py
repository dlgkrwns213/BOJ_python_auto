import sys
input = sys.stdin.readline
near = [(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1) if i or j]


def dfs(sx, sy):
    stack = [(sx, sy)]

    while stack:
        x, y = stack.pop()
        for a, b in near:
            nx, ny = x+a, y+b
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited[nx][ny]:
                continue

            visited[nx][ny] = 1
            stack.append((nx, ny))


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

visited = [[0 if board[i][j] else 1 for j in range(m)] for i in range(n)]
cnt = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            cnt += 1
            dfs(i, j)

print(cnt)