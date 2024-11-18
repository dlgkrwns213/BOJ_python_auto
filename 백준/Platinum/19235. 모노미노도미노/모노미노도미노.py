# https://www.acmicpc.net/problem/20061
import sys
input = sys.stdin.readline


def check_score(board):
    global score
    for i in range(5, 1, -1):
        if all(board[i]):
            score += 1
            for j in range(4):
                board[i][j] = 0
            if all(board[i-1]):
                score += 1
                for j in range(4):
                    board[i-1][j] = 0

            for up in range(i-1, -1, -1):
                for j in range(4):
                    if not board[up][j]:
                        continue

                    if up > 0 and board[up][j] == board[up-1][j]:
                        for up_down in range(up + 1, 7):
                            if board[up_down][j]:
                                tmp1, tmp2 = board[up][j], board[up-1][j]
                                board[up][j], board[up-1][j] = 0, 0
                                board[up_down-1][j], board[up_down-2][j] = tmp1, tmp2
                                break
                    if j < 3 and board[up][j] == board[up][j+1]:
                        for up_down in range(up + 1, 7):
                            if board[up_down][j] or board[up_down][j+1]:
                                tmp1, tmp2 = board[up][j], board[up][j+1]
                                board[up][j], board[up][j+1] = 0, 0
                                board[up_down-1][j], board[up_down-1][j+1] = tmp1, tmp2

                                break

                    else:
                        for up_down in range(up+1, 7):
                            if board[up_down][j]:
                                tmp = board[up][j]
                                board[up][j] = 0
                                board[up_down-1][j] = tmp
                                break

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
            board[i][j] = block_number
            return


def horizontal(board, j):
    for i in range(1, 6):
        if board[i+1][j] or board[i+1][j+1]:
            board[i][j], board[i][j+1] = block_number, block_number
            return


def vertical(board, j):
    for i in range(5):
        if board[i+2][j]:
            board[i][j], board[i+1][j] = block_number, block_number
            return


green, blue = [[0]*4 for _ in range(7)], [[0]*4 for _ in range(7)]
for j in range(4):
    green[6][j] = -1
    blue[6][j] = -1

score = 0
for block_number in range(1, int(input())+1):
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

    while check_score(green): ...
    while check_score(blue): ...

    check_break(green)
    check_break(blue)

print(score)
total = lambda board: sum(map(lambda line: sum(map(lambda x: 1 if x else 0, line)), board))
print(total(blue[:-1]) + total(green[:-1]))