# https://www.acmicpc.net/problem/26598
import sys
from collections import deque
input = sys.stdin.readline


def find(sx, sy, want):
    if sx and board[sx-1][sy] == want:
        return False
    if sy and board[sx][sy-1] == want:
        return False

    for lx in range(sx, n):
        if board[lx][sy] != want:
            lx -= 1
            break

    for ly in range(sy, m):
        if board[sx][ly] != want:
            ly -= 1
            break

    for x in range(sx, lx+1):
        for y in range(sy, ly+1):
            if board[x][y] != want or (board[x][y] == want and visited[x][y]):
                return False
            visited[x][y] = 1

    return True


n, m = map(int, input().split())
board = [input().rstrip() for _ in range(n)]

visited = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            if not find(i, j, board[i][j]):
                print('BaboBabo')
                exit(0)
print('dd')