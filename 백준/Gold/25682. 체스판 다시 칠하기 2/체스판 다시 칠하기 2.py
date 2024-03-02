# https://www.acmicpc.net/problem/25682
import sys
input = sys.stdin.readline


def checking(x):
    diff = [[0]*(m+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(m):
            if (i + j) % 2 == x:
                diff[i][j] = 1 if board[i][j] == 'B' else 0
            else:
                diff[i][j] = 1 if board[i][j] == 'W' else 0

    for i in range(1, n):
        diff[i][0] += diff[i-1][0]
    for j in range(1, m):
        diff[0][j] += diff[0][j-1]
    for i in range(1, n):
        for j in range(1, m):
            diff[i][j] += diff[i][j-1] + diff[i-1][j] - diff[i-1][j-1]

    mn = n*m
    for i in range(k-1, n):
        for j in range(k-1, m):
            mn = min(mn, diff[i][j] - diff[i-k][j] - diff[i][j-k] + diff[i-k][j-k])

    return mn


n, m, k = map(int, input().split())
board = [input().rstrip() for _ in range(n)]

print(min(checking(0), checking(1)))