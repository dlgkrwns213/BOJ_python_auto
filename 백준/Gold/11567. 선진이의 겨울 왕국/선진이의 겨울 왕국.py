# https://www.acmicpc.net/problem/11567
import sys
from collections import deque
input = sys.stdin.readline
go = ((-1, 0), (1, 0), (0, 1), (0, -1))


def bfs() -> bool:
    q = deque()
    q.append((r1, c1))

    while q:
        x, y = q.popleft()

        for a, b in go:
            nx, ny = x+a, y+b

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if board[nx][ny]:
                if (nx, ny) == (r2, c2):
                    return True
                else:
                    continue

            board[nx][ny] = 1
            q.append((nx, ny))


n, m = map(int, input().split())
board = [[1 if x == 'X' else 0 for x in input().rstrip()] for _ in range(n)]
r1, c1 = map(lambda x: int(x)-1, input().split())
r2, c2 = map(lambda x: int(x)-1, input().split())

print('YES' if bfs() else 'NO')