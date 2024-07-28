# https://www.acmicpc.net/problem/5931
import sys
from collections import deque
input = sys.stdin.readline
go = ((-1, 0), (1, 0), (0, -1), (0, 1))


def numbering(sx, sy, number):
    board[sx][sy] = number

    q = deque()
    q.append((sx, sy))

    edge = set()
    while q:
        x, y = q.popleft()
        for a, b in go:
            nx, ny = x+a, y+b
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if board[nx][ny] == '.':
                edge.add((x, y))
            if board[nx][ny] != 'X':
                continue

            board[nx][ny] = number
            q.append((nx, ny))

    edges.append(list(edge))


def find(number):
    visited = [[0]*m for _ in range(n)]

    q = deque()
    for x, y in edges[number]:
        q.append((x, y, 0))

    while q:
        x, y, cnt = q.popleft()
        for a, b in go:
            nx, ny = x+a, y+b
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if board[nx][ny] == '.':
                if visited[nx][ny]:
                    continue

                visited[nx][ny] = 1
                q.append((nx, ny, cnt+1))
            elif board[nx][ny] != number:
                return cnt


n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]

count, edges = 0, []
for i in range(n):
    for j in range(m):
        if board[i][j] == 'X':
            numbering(i, j, count)
            count += 1

mn = m*n
for num in range(count):
    mn = min(mn, find(num))
print(mn)