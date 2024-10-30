# https://www.acmicpc.net/problem/10429
go = ((-1, 0), (1, 0), (0, -1), (0, 1))


def backtracking(cnt, x, y, visited, make):
    global ans
    if ans:
        return
    if cnt == 2*m-1:
        if eval(make) == n:
            ans = [(x, y)]
            while (x, y) != (si, sj):
                x, y = log[x][y]
                ans.append((x, y))

        return

    for a, b in go:
        nx, ny = x+a, y+b
        if nx < 0 or nx >= 3 or ny < 0 or ny >= 3:
            continue
        nxt_bit = 1 << 3*nx + ny

        if visited & nxt_bit:
            continue

        log[nx][ny] = x, y
        backtracking(cnt+1, nx, ny, visited | nxt_bit, make+board[nx][ny])


n, m = map(int, input().split())
board = [input() for _ in range(3)]

ans, log = '', [[(3, 3)]*3 for _ in range(3)]
for idx in range(0, 10, 2):
    si, sj = divmod(idx, 3)
    backtracking(1, si, sj, 1 << 3*si + sj, board[si][sj])

if ans:
    print(1)
    print('\n'.join(map(lambda line: ' '.join(map(str, line)), ans[::-1])))
else:
    print(0)