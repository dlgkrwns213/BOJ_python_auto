# https://www.acmicpc.net/problem/4056
import sys
input = sys.stdin.readline


def backtracking(idx):
    global possible
    if idx == 5:
        for i in range(9):
            if len(set(board[i][j] for j in range(9))) != 9:
                return False
        for j in range(9):
            if len(set(board[i][j] for i in range(9))) != 9:
                return False
        for i in range(3):
            for j in range(3):
                if len(set(board[3*i+a][3*j+b] for a in range(3) for b in range(3))) != 9:
                    return False

        possible = True
        ans.append('\n'.join(map(lambda line: ''.join(map(str, line)), board)))
        return

    x, y = zeros[idx]
    w = {board[i][y] for i in range(9)}
    h = {board[x][i] for i in range(9)}
    rx, ry = x // 3 * 3, y // 3 * 3
    t = {board[rx+i][ry+j] for i in range(3) for j in range(3)}

    for num in range(1, 10):
        if num in w or num in h or num in t:
            continue

        board[x][y] = num
        backtracking(idx+1)
        board[x][y] = 0


ans = []
for _ in range(int(input())):
    board = [list(map(int, input().rstrip())) for _ in range(9)]

    zeros = [(i, j) for i in range(9) for j in range(9) if not board[i][j]]
    possible = False
    backtracking(0)
    if not possible:
        ans.append('Could not complete this grid.')

print('\n\n'.join(ans))