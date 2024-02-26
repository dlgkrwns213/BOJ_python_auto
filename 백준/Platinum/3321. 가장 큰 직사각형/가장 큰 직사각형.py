import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [[int(x) for x in input().rstrip()] for _ in range(n)]

for j in range(m):
    for i in range(1, n):
        if board[i][j]:
            board[i][j] += board[i-1][j]
    
for line in board:
    line.sort(reverse=True)
    
ans = -1
for line in  board:
    for j, v in enumerate(line):
        ans = max(ans, v*(j+1))
print(ans)