import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = float('inf')


def dijkstra():
    go = ((-1, 0), (1, 0), (0, -1), (0, 1))

    distances = [[INF]*m for _ in range(n)]
    distances[0][0] = 0

    hq = []
    heappush(hq, (0, 0, 0))

    while hq:
        gap, x, y = heappop(hq)

        if distances[x][y] < gap:
            continue
        if (x, y) == (n-1, m-1):
            return gap

        for a, b in go:
            nx, ny = x+a, y+b
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            nxt_gap = max(board[nx][ny] - board[x][y], gap)

            if distances[nx][ny] > nxt_gap:
                distances[nx][ny] = nxt_gap
                heappush(hq, (nxt_gap, nx, ny))


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

print(dijkstra())