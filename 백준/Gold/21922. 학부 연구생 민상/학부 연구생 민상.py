# https://www.acmicpc.net/problem/21922
import sys
input = sys.stdin.readline
go = ((-1, 0), (1, 0), (0, -1), (0, 1))


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
        if not now:
            continue

        if d == 0:
            if now == 2:
                break
            elif now == 3:
                d = 3
            elif now == 4:
                d = 2
        elif d == 1:
            if now == 2:
                break
            elif now == 3:
                d = 2
            elif now == 4:
                d = 3
        elif d == 2:
            if now == 1:
                break
            elif now == 3:
                d = 1
            elif now == 4:
                d = 0
        else:
            if now == 1:
                break
            elif now == 3:
                d = 0
            elif now == 4:
                d = 1


n, m = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]

is_cool = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if room[i][j] == 9:
            is_cool[i][j] = 1
            for init_d in range(4):
                simulation(i, j, init_d)

print(sum(map(sum, is_cool)))