import sys
from heapq import heappush, heappop
input = sys.stdin.readline
go = [(-1, 0), (1, 0), (0, -1), (0, 1)]
INF = 10**12


def dijkstra(sx, sy):
    dist = [[INF]*n for _ in range(n)]
    pq = [(0, sx, sy)]
    dist[sx][sy] = 0
    while pq:
        cost, x, y = heappop(pq)
        if dist[x][y] < cost:
            continue
        for a, b in go:
            nx, ny = x+a, y+b
            if 0 <= nx < n and 0 <= ny < n:
                nxt_cost = cost + grid[nx][ny]
                if dist[nx][ny] > nxt_cost:
                    dist[nx][ny] = nxt_cost
                    heappush(pq, (nxt_cost, nx, ny))
    return dist


n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

points = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == -1:
            base = (i, j)
            grid[i][j] = 0
        elif grid[i][j] == 0:
            points.append((i, j))

points = [base] + points
m = len(points)


dist_matrix = [[INF]*m for _ in range(m)]
for i, (x, y) in enumerate(points):
    d = dijkstra(x, y)
    for j, (tx, ty) in enumerate(points):
        dist_matrix[i][j] = d[tx][ty]

all_catch = (1 << (m - 1)) - 1
dp = [[INF]*m for _ in range(1 << (m-1))]
dp[0][0] = 0

for mask in range(1 << (m-1)):
    for u in range(m):
        if dp[mask][u] == INF:
            continue
        for v in range(1, m):
            if mask & (1 << (v-1)):
                continue
            nxt_mask = mask | (1 << (v - 1))
            dp[nxt_mask][v] = min(dp[nxt_mask][v], dp[mask][u] + dist_matrix[u][v])

ans = INF
for u in range(m):
    ans = min(ans, dp[all_catch][u] + dist_matrix[u][0])

print(ans)