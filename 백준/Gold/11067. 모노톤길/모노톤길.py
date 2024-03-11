# https://www.acmicpc.net/problem/11067
import sys
input = sys.stdin.readline

ans = []
for _ in range(int(input())):
    n = int(input())
    locations = [list(map(int, input().split())) for _ in range(n)]

    # x 정렬, x 마다 y 정렬
    y_loc = dict()
    for x, y in locations:
        if x in y_loc:
            y_loc[x].append(y)
        else:
            y_loc[x] = [y]
    x_loc = sorted(y_loc.keys())
    for x in y_loc:
        y_loc[x].sort()

    # 이전 y와 현재 y들 중에서 최소가 같으면 순정렬, 최대가 같으면 역정렬
    loc, idx = [()] * n, 0
    bef_y = 0
    for x in x_loc:
        if y_loc[x][0] == bef_y:
            for y in y_loc[x]:
                loc[idx] = (x, y)
                idx += 1
        else:
            for y in y_loc[x][::-1]:
                loc[idx] = (x, y)
                idx += 1
        bef_y = y

    for idx in map(int, input().split()[1:]):
        a, b = loc[idx-1]
        ans.append(f'{a} {b}')

print('\n'.join(ans))