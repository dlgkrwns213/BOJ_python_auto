# https://www.acmicpc.net/problem/16933
import sys
from collections import deque
input = sys.stdin.readline
INF = 11


def bfs():
    go = ((-1, 0), (1, 0), (0, 1), (0, -1))
    q = deque()
    q.append((0, 0, 0, 1, 1))  # x y broken day cnt

    visited = [[[INF]*m for _ in range(n)] for _ in range(2)]
    visited[1][0][0] = 0

    while q:
        x, y, broken, day, cnt = q.popleft()
        if (x, y) == (n-1, m-1):
            return cnt

        if not day:
            for a, b in go:
                nx, ny = x+a, y+b
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if board[nx][ny]:
                    q.append((x, y, broken, 1, cnt+1))
                    break
                    
        for a, b in go:
            nx, ny = x+a, y+b
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if broken >= visited[1-day][nx][ny]:
                continue

            if board[nx][ny]:
                if day:
                    if broken < k and broken+1 < visited[0][nx][ny]:
                        visited[0][nx][ny] = broken + 1
                        q.append((nx, ny, broken+1, 0, cnt+1))
            else:
                visited[1-day][nx][ny] = broken
                q.append((nx, ny, broken, 1-day, cnt+1))

    return -1


n, m, k = map(int, input().split())
board = [[int(x) for x in input().rstrip()] for _ in range(n)]

print(bfs())

