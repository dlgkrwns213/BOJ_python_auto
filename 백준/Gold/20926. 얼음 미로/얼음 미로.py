# https://www.acmicpc.net/problem/20926
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
INF = float('inf')


def find_start_end():
    si, sj, ei, ej = 0, 0, 0, 0
    for i, line in enumerate(board):
        for j, v in enumerate(line):
            if v == 'T':
                si, sj =  i, j
                times[i][j] = INF
            elif v == 'E':
                times[i][j] = -1
                ei, ej = i, j
            elif v == 'R':
                times[i][j] = -2
            elif v == 'H':
                times[i][j] = -3
    return si, sj, ei, ej


def dijkstra(sx, sy, ex, ey):
    go = ((-1, 0), (1, 0), (0, -1), (0, 1))

    distances = [[INF]*w for _ in range(h)]
    distances[sx][sy] = 0

    hq = []
    heappush(hq, (0, sx, sy))

    while hq:
        time, x, y = heappop(hq)
        if (x, y) == (ex, ey):
            return time

        if distances[x][y] < time:
            continue

        for a, b in go:
            nx, ny = x+a, y+b

            nxt_time = time
            while True:
                if nx < 0 or nx >= h or ny < 0 or ny >= h or times[nx][ny] == -3:
                    nxt_time = INF
                    break
                if times[nx][ny] == -2:
                    break
                if times[nx][ny] == -1:
                    nx += a
                    ny += b
                    break

                nxt_time += times[nx][ny]
                nx += a
                ny += b
            nx -= a
            ny -= b
            if distances[nx][ny] > nxt_time:
                distances[nx][ny] = nxt_time
                heappush(hq, (nxt_time, nx, ny))

    return INF



w, h = map(int, input().split())
board = [input().rstrip() for _ in range(h)]
times = [list(map(lambda time: int(time) if time.isdigit() else -1, line)) for line in board]

ans = dijkstra(*find_start_end())
print(ans if ans != INF else -1)