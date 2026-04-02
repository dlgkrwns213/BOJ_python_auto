INF = float('inf')
go = ((-1, 0), (1, 0), (0, -1), (0, 1))


def backtracking(now, time, apple, now_cant):
    global mn_time
    if mn_time < time:
        return
    if apple == 3:
        mn_time = time
        return

    x, y = divmod(now, 5)
    for a, b in go:
        nx, ny = x+a, y+b
        if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
            continue

        nxt = nx * 5 + ny
        if now_cant & (1 << nxt):
            continue

        backtracking(nxt, time+1, apple + board[nx][ny], now_cant | (1 << nxt))


board = [list(map(int, input().split())) for _ in range(5)]
r, c = map(int, input().split())

cant = 0
for i in range(25):
    x, y = divmod(i, 5)
    if board[x][y] == -1:
        cant |= 1 << i

mn_time = INF
start = r * 5 + c
backtracking(start, 0, 0, cant | (1 << start))
print(mn_time if mn_time != INF else -1)