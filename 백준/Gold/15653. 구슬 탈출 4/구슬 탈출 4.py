from collections import deque


def move(x, y, dx, dy):
    move_count = 0
    while board[x + dx][y + dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        move_count += 1
    return x, y, move_count


def bfs(rx, ry, bx, by):
    queue = deque([(rx, ry, bx, by, 0)])
    visited = set([(rx, ry, bx, by)])

    while queue:
        rx, ry, bx, by, cnt = queue.popleft()

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nrx, nry, r_move = move(rx, ry, dx, dy)
            nbx, nby, b_move = move(bx, by, dx, dy)

            if board[nbx][nby] != 'O':
                if board[nrx][nry] == 'O':
                    return cnt + 1

                if nrx == nbx and nry == nby:
                    if r_move > b_move:
                        nrx -= dx
                        nry -= dy
                    else:
                        nbx -= dx
                        nby -= dy

                if (nrx, nry, nbx, nby) not in visited:
                    visited.add((nrx, nry, nbx, nby))
                    queue.append((nrx, nry, nbx, nby, cnt + 1))

    return -1


n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

ri, rj, bi, bj = 0, 0, 0, 0

for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            ri, rj = i, j
        elif board[i][j] == 'B':
            bi, bj = i, j

result = bfs(ri, rj, bi, bj)
print(result)
