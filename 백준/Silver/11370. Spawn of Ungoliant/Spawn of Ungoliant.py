import sys
from collections import deque
input = sys.stdin.readline
go = ((-1, 0), (1, 0), (0, 1), (0, -1))

while True:
    w, h = map(int, input().split())
    if not w and not h:
        break

    board = [list(input().rstrip()) for _ in range(h)]
    starts = [(i, j) for i in range(w) for j in range(h) if board[j][i] =='S']

    q = deque(starts)
    while q:
        x, y = q.popleft()
        for a, b in go:
            nx, ny = x+a, y+b

            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if board[nx][ny] != 'T':
                continue

            board[nx][ny] = 'S'
            q.append((nx, ny))

    print('\n'.join(map(lambda line: ''.join(line), board)))