# https://www.acmicpc.net/problem/21772
import sys
input = sys.stdin.readline
go = ((-1, 0), (1, 0), (0, -1), (0, 1))


def find_kahee():
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'G':
                return i, j


def backtracking(move, x, y, sw_list):
    global mx
    if move == t:
        mx = max(mx, len(set(sw_list)))
        return

    for a, b in go:
        nx, ny = x+a, y+b
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            continue
        if board[nx][ny] == '#':
            continue

        if board[nx][ny] == 'S':
            sw_list.append(nx*c+ny)
            backtracking(move+1, nx, ny, sw_list)
            sw_list.pop()
        else:
            backtracking(move+1, nx, ny, sw_list)


r, c, t = map(int, input().split())
board = [input().rstrip() for _ in range(r)]

sx, sy = find_kahee()
mx = 0
backtracking(0, sx, sy, [])
print(mx)