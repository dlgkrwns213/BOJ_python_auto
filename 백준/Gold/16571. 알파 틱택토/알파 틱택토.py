# https://www.acmicpc.net/problem/16571
def checking(idx, player):
    a, b, c, d, e, f, g, h, i = sum(board, [])
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
        x, y = divmod(i, 3)
        if board[x][y]:
            continue

        board[x][y] = player
        if checking(i, player):
            ret = 1
        else:
            ret = max(ret, backtracking(rest-1, 3-player))
        board[x][y] = 0

    return -ret


board = [list(map(int, input().split())) for _ in range(3)]
zero = sum(map(lambda line: line.count(0), board))
one = sum(map(lambda line: line.count(1), board))
two = sum(map(lambda line: line.count(2), board))

first = 1 if one == two else 2

ans = backtracking(zero, first)
print('DLW'[ans])