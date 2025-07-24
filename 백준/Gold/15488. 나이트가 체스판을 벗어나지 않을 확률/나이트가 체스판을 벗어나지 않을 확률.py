# https://www.acmicpc.net/problem/15488
from copy import deepcopy
bef = ((-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1))

n, x, y, k = map(int, input().split())

now = [[0]*n for _ in range(n)]
now[x-1][y-1] = 1
for _ in range(k):
    nxt = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            ret = 0
            for dx, dy in bef:
                nx = i + dx
                ny = j + dy
                if 0 <= nx < n and 0 <= ny < n:
                    ret += now[nx][ny]
            nxt[i][j] = ret

    now = deepcopy(nxt)

print(sum(map(sum, now)) / (8 ** k))