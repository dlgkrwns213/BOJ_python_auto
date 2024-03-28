# https://www.acmicpc.net/problem/30678
def backtracking(size, x, y):
    nxt_size = size // 5
    for i in draw_idx:
        a, b = divmod(i, 5)

        nx, ny = x + a * nxt_size, y + b * nxt_size
        if nxt_size > 1:
            backtracking(nxt_size, nx, ny)
        else:
            board[nx][ny] = '*'


n = int(input())
init_size = 5 ** n

board = [[' ']*init_size for _ in range(init_size)]
draw_idx = [2, 7, 10, 11, 12, 13, 14, 16, 17, 18, 21, 23]

backtracking(init_size, 0, 0)

print('\n'.join(map(lambda line: ''.join(line), board)))