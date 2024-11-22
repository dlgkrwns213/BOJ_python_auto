# https://www.acmicpc.net/problem/1577
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [[0]*(m+1) for _ in range(n+1)]
cants = set()
for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    if a > c:
        a, c = c, a
    if b > d:
        b, d = d, b
    cants.add((a, b, c, d))

board[0][0] = 1
for i in range(n+1):
    for j in range(m+1):
        if not (i or j):
            continue
        ret = 0
        if (i-1, j, i, j) not in cants:
            ret = board[i-1][j]
        if (i, j-1, i, j) not in cants:
            ret += board[i][j-1]

        board[i][j] = ret

print(board[n][m])