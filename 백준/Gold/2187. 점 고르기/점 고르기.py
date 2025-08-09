# https://www.acmicpc.net/problem/2187
import sys
input = sys.stdin.readline
directs = ((-1, -1), (-1, 1), (1, -1), (1, 1))


def get_value(point, x, y):
    lx = point[0] + (a-1) * x
    ly = point[1] + (b-1) * y

    mx, mn = point[2], point[2]
    for another in points:
        if ((lx <= another[0] <= point[0]) or (point[0] <= another[0] <= lx)) and ((ly <= another[1] <= point[1]) or (point[1] <= another[1] <= ly)):
            mx = max(mx, another[2])
            mn = min(mn, another[2])

    return mx - mn


def get_max_four_value(point: list):
    return max(map(lambda d: get_value(point, *d), directs))


n, a, b = map(int, input().split())
points = [list(map(int, input().split())) for _ in range(n)]

print(max(map(get_max_four_value, points)))