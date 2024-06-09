import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(n)]

cnt = 0
for i in range(200, -1, -1):
    for j in range(200, -1, -1):
        if i >= n or j >= m:
            continue

        if board[i][j]:
            cnt += 1
            for a in range(i+1):
                for b in range(j+1):
                    board[a][b] ^= 1
            board[i][j] = 0

print(cnt)