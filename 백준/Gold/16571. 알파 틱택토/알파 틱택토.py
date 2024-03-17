# https://www.acmicpc.net/problem/16571
def checking(idx, player):
    a, b, c, d, e, f, g, h, i = board
    if idx == 0:
        if (player, player) in ((b, c), (d, g), (e, i)):
            return True
    elif idx == 1:
        if (player, player) in ((a, c), (e, h)):
            return True
    elif idx == 2:
        if (player, player) in ((a, b), (f, i), (e, g)):
            return True
    elif idx == 3:
        if (player, player) in ((a, g), (e, f)):
            return True
    elif idx == 4:
        if (player, player) in ((d, f), (b, h), (a, i), (c, g)):
            return True
    elif idx == 5:
        if (player, player) in ((d, e), (c, i)):
            return True
    elif idx == 6:
        if (player, player) in ((h, i), (a, d), (c, e)):
            return True
    elif idx == 7:
        if (player, player) in ((g, i), (b, e)):
            return True
    elif idx == 8:
        if (player, player) in ((g, h), (c, f), (a, e)):
            return True
    return False


def backtracking(rest, player):
    if not rest:
        return 0

    ret = -2
    for i in range(9):
        if board[i]:
            continue

        board[i] = player
        if checking(i, player):
            ret = 1
        else:
            ret = max(ret, backtracking(rest-1, 3-player))
        board[i] = 0

    return -ret


board = sum([list(map(int, input().split())) for _ in range(3)], [])
zero = board.count(0)
one = board.count(1)
two = board.count(2)

first = 1 if one == two else 2

ans = backtracking(zero, first)
print('DLW'[ans])