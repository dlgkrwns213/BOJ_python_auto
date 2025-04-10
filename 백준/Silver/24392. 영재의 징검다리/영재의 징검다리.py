import sys
input = sys.stdin.readline
MOD = int(1e9) + 7

n,  m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

now = board[-1].copy() + [0]
for i in range(n-2, -1, -1):
    nxt = [0] * (m+1)
    for j in range(m):
        nxt[j] = (now[j-1] + now[j] + now[j+1]) % MOD if board[i][j] else 0

    now = nxt

print(sum(now) % MOD)