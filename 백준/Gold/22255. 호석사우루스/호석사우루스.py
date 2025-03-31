# https://www.acmicpc.net/problem/22255
import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = float('inf')


def dijkstra():
    go = [((-1, 0), (1, 0), (0, -1), (0, 1)), ((-1, 0), (1, 0)), ((0, -1), (0, 1))]

    distances = [[[INF]*3 for _ in range(m)] for _ in range(n)]
    distances[sx][sy][1] = 0

    hq = []
    heappush(hq, (0, 1, sx, sy))

    while hq:
        impact, time, x, y = heappop(hq)
        if (x, y) == (ex, ey):
            return impact
        if impacts[x][y] == -1:
            continue
        if distances[x][y][time] < impact:
            continue

        nxt_time = (time + 1) % 3
        for a, b in go[time]:
            nx, ny = x+a, y+b
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            nxt_impact = impact + impacts[nx][ny]
            if distances[nx][ny][nxt_time] > nxt_impact:
                distances[nx][ny][nxt_time] = nxt_impact
                heappush(hq, (nxt_impact, nxt_time, nx, ny))

    return -1


n, m = map(int, input().split())
sx, sy, ex, ey = map(lambda x: int(x)-1, input().split())
impacts = [list(map(int, input().split())) for _ in range(n)]

print(dijkstra())