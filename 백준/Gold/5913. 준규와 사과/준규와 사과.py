# https://www.acmicpc.net/problem/5913
import sys
input = sys.stdin.readline
go = ((-1, 0), (1, 0), (0, -1), (0, 1))


def backtracking(rest, jx, jy, hx, hy):
    global cnt

    for a, b in go:
        njx, njy = jx+a, jy+b
        if njx < 0 or njx >= 5 or njy < 0 or njy >= 5:
            continue
        if board[njx][njy]:
            continue

        for c, d in go:
            nhx, nhy = hx+c, hy+d
            if nhx < 0 or nhx >= 5 or nhy < 0 or nhy >= 5:
                continue
            if board[nhx][nhy]:
                continue

            if (nhx, nhy) == (njx, njy):
                if not rest:
                    cnt += 1
                continue

            board[njx][njy] = 1
            board[nhx][nhy] = 1
            backtracking(rest-1, njx, njy, nhx, nhy)
            board[nhx][nhy] = 0
            board[njx][njy] = 0


board = [[0]*5 for _ in range(5)]
k = int(input())
for _ in range(k):
    i, j = map(lambda _: int(_)-1, input().split())
    board[i][j] = 1
board[0][0], board[4][4] = 1, 1

cnt = 0
backtracking(11-k//2, 0, 0, 4, 4)
print(cnt)