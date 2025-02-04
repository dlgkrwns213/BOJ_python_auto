# https://www.acmicpc.net/problem/5213
import sys
from collections import deque
input = sys.stdin.readline
go = ((-1, 0), (1, 0), (0, -1), (0, 1))


def bfs():
    visited = [[0]*2*n for _ in range(n)]
    visited[0][0], visited[0][1] = 1, 1

    q = deque()
    q.append((0, 0, 1))
    q.append((0, 1, 1))

    log = [-1] * (colors[-1][-2] + 1)
    log[1] = 0

    while q:
        x, y, c = q.popleft()
        for a, b in go:
            nx, ny = x+a, y+b
            if nx < 0 or nx >= n or ny < 0 or ny >= 2*n:
                continue
            if visited[nx][ny]:
                continue

            if board[x][y] == board[nx][ny]:
                nc = colors[nx][ny]
                if (nx+ny) % 2:
                    if not visited[nx][ny-1]:
                        visited[nx][ny-1] = 1
                        q.append((nx, ny-1, nc))
                else:
                    if not visited[nx][ny+1]:
                        visited[nx][ny+1] = 1
                        q.append((nx, ny+1, nc))
                visited[nx][ny] = 1
                q.append((nx, ny, nc))
                log[nc] = c

    # 가장 큰 타일로부터 처음까지 경로 구하기
    lc = colors[-1][-2]
    while log[lc] == -1:
        lc -= 1

    ret = [lc]
    while log[lc]:
        lc = log[lc]
        ret.append(lc)
    return ret[::-1]


n = int(input())

board = [[-1] * 2 * n for _ in range(n)]
colors, color = [[-1] * 2 * n for _ in range(n)], 1
for i in range(n):
    if i % 2:
        for j in range(1, 2*n-1, 2):
            a, b = map(int, input().split())
            board[i][j], board[i][j+1] = a, b
            colors[i][j], colors[i][j+1] = color, color
            color += 1
    else:
        for j in range(0, 2*n, 2):
            a, b = map(int, input().split())
            board[i][j], board[i][j+1] = a, b
            colors[i][j], colors[i][j+1] = color, color
            color += 1

ans = bfs()
print(len(ans))
print(' '.join(map(str, ans)))