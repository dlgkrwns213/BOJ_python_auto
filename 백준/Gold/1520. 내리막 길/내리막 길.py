import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
go = ((-1, 0), (1, 0), (0, -1), (0, 1))


def dfs(x:int, y:int):
    global cnt
    if x == n-1 and y==m-1:
        return 1
    
    if dp[x][y] != -1:
        return dp[x][y]
    
    dp[x][y] = 0
    for a, b in go:
        nx, ny = x+a, y+b
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if board[x][y] <= board[nx][ny]:
            continue
            
        dp[x][y] += dfs(nx, ny)
            
    return dp[x][y]
    

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dp = [[-1]*m for _ in range(n)]
cnt = 0

print(dfs(0, 0))