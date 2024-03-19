# https://www.acmicpc.net/problem/4574
import sys
input = sys.stdin.readline


def str2location(s_loc: str) -> tuple:
    x = ord(s_loc[0]) - ord('A')
    y = int(s_loc[1]) - 1
    return x, y


def checking(x, y, num):
    for i in range(9):
        if board[i][y] == num:
            return False
    for j in range(9):
        if board[x][j] == num:
            return False

    a, b = (x // 3) * 3, (y // 3) * 3
    for i in range(a, a+3):
        for j in range(b, b+3):
            if board[i][j] == num:
                return False

    return True


def backtracking(idx, use):
    global finish
    if finish:
        return
    if idx == 81:
        for line in board[:-1]:
            print(''.join(map(str, line[:-1])))
        finish = True
        return

    x, y = divmod(idx, 9)
    if board[x][y]:
        backtracking(idx+1, use)
        return

    for num in range(1, 10):
        if not checking(x, y, num):
            continue
        board[x][y] = num

        for nx, ny in ((x+1, y), (x, y+1)):
            if board[nx][ny]:
                continue

            for near_num in range(1, 10):
                if not checking(nx, ny, near_num):
                    continue

                p, q = num, near_num
                if p > q:
                    p, q = q, p

                if use & (1 << (10 * p + q)):
                    continue

                board[nx][ny] = near_num
                backtracking(idx+1, use | 1 << (10 * p + q))
                board[nx][ny] = 0

        board[x][y] = 0


for tc in range(1, int(1e6)):
    n = int(input())
    if not n:
        break
    print(f'Puzzle {tc}')

    board = [[0]*10 for _ in range(10)]
    for i in range(10):
        board[9][i], board[i][9] = 10, 10

    use = 0
    for _ in range(n):
        a, axy, b, bxy = input().split()
        a, b = map(int, (a, b))
        ax, ay = str2location(axy)
        bx, by = str2location(bxy)

        use |= 1 << (a * 10 + b)
        board[ax][ay] = a
        board[bx][by] = b

    for i, loc in enumerate(input().split()):
        loc_x, loc_y = str2location(loc)
        board[loc_x][loc_y] = i+1

    finish = False
    backtracking(0, use)