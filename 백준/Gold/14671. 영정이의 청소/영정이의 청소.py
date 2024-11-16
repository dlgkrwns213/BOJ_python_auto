# https://www.acmicpc.net/problem/14671
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
board = [0, 0, 0, 0]
for _ in range(k):
    x, y = map(lambda a: int(a)%2, input().split())
    board[2*x+y] = 1

print('YES' if sum(board) == 4 else 'NO')