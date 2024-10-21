import sys
input = sys.stdin.readline
go = [(-1, 0), (1, 0), (0, -1), (0, 1)]
rotate = [
    [0, 0, -1, 3, 2],
    [0, 1, -1, 2, 3],
    [0, -1, 2, 1, 0],
    [0, -1, 3, 0, 1]
]


def simulation(sx, sy, d):
    x, y = sx, sy
    while True:
        a, b = go[d]
        x += a
        y += b
        if x < 0 or x >= n or y < 0 or y >= m:
            break

        is_cool[x][y] = 1
        now = room[x][y]
        if now == 9:
            break
        if now == 0:
            continue

        d = rotate[d][now]
        if d == -1:
            break


n, m = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]

is_cool = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if room[i][j] == 9:
            is_cool[i][j] = 1
            for init_d in range(4):
                simulation(i, j, init_d)

print(sum(map(sum, is_cool)))