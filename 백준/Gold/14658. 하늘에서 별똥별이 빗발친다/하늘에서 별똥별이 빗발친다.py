# https://www.acmicpc.net/problem/14658
import sys
input = sys.stdin.readline

n, m, l, k = map(int, input().split())
stars = sorted(list(map(int, input().split())) for _ in range(k))

mx = 0
for left, locations in enumerate(stars):
    # x를 기준으로 가능한 y에 대해 모아줌
    lx, ly = locations

    y_locations = []
    right = left
    while right < k:
        rx, ry = stars[right]
        if rx - lx > l:
            break

        y_locations.append(ry)
        right += 1

    # y를 기준으로 막을 수 있는 최대 구하기
    y_locations.sort()
    cnt = len(y_locations)

    up = 0
    for down, y in enumerate(y_locations):
        while up < cnt and y_locations[up] - y <= l:
            up += 1

        mx = max(mx, up - down)

print(k-mx)