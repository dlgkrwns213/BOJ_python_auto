# https://www.acmicpc.net/problem/20061
import sys
input = sys.stdin.readline


def check_score(board):
    global score
    for i in range(5, 1, -1):
        if all(board[i]):
            score += 1
            for up in range(i-1, -1, -1):
                for j in range(4):
                    board[up+1][j] = board[up][j]
            return True
    return False


def check_break(board):
    cnt = 0
    if any(board[0]):
        cnt = 2
    elif any(board[1]):
        cnt = 1

    if not cnt:
        return

    for i in range(5, 1, -1):
        for j in range(4):
            board[i][j] = board[i-cnt][j]

    for i in range(cnt):
        for j in range(4):
            board[1-i][j] = 0


def one(board, j):
    for i in range(1, 6):
        if board[i+1][j]:
            board[i][j] = 1
            return


def horizontal(board, j):
    for i in range(1, 6):
        if board[i+1][j] or board[i+1][j+1]:
            board[i][j], board[i][j+1] = 1, 1
            return


def vertical(board, j):
    for i in range(5):
        if board[i+2][j]:
            board[i][j], board[i+1][j] = 1, 1
            return


green, blue = [[0]*4 for _ in range(7)], [[0]*4 for _ in range(7)]
for j in range(4):
    green[6][j] = 1
    blue[6][j] = 1

score = 0
for _ in range(int(input())):
    t, x, y = map(int, input().split())
    if t == 1:
        one(green, y)
        one(blue, x)
    elif t == 2:
        horizontal(green, y)
        vertical(blue, x)
    else:
        vertical(green, y)
        horizontal(blue, x)

    if check_score(green):
        check_score(green)
    if check_score(blue):
        check_score(blue)

    check_break(green)
    check_break(blue)

print(score)
print(sum(map(sum, blue[:-1])) + sum(map(sum, green[:-1])))