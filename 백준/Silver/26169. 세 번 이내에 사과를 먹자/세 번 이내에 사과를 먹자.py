go = ((-1, 0), (1, 0), (0, -1), (0, 1))


def backtracking(move, x, y, eat, visited):
    global possible
    possible = possible | (eat >= 2)
    if move == 3:
        return

    for a, b in go:
        nx, ny = x+a, y+b
        if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
            continue
        if board[nx][ny] == -1:
            continue
        if visited & (1 << (5 * nx + ny)):
            continue

        backtracking(move+1, nx, ny, eat + board[nx][ny], visited | (1 << (5*nx+ny)))


board = [list(map(int, input().split())) for _ in range(5)]
r, c = map(int, input().split())

possible = 0
backtracking(0, r, c, 0, 1 << (r*5+c))
print(possible)