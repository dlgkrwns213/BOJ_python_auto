# https://www.acmicpc.net/problem/12100

from copy import deepcopy

def backtracking(board, direction, times):
    global m
    
    if times == 5:
        m = max(m, max(map(max, board)))
        return

    if direction == 0:  # left
        for i in range(n):
            idx = 0
            for j in range(1, n):
                if not board[i][j]:
                    continue
                
                tmp = board[i][j]
                board[i][j] = 0
                
                if board[i][idx] == tmp:
                    board[i][idx] = 2*tmp
                    idx += 1
                elif not board[i][idx]:
                    board[i][idx] = tmp
                else:
                    idx += 1
                    board[i][idx] = tmp            
    
    elif direction == 1:  # right
        for i in range(n):
            idx = n-1
            for j in range(n-2, -1, -1):
                if not board[i][j]:
                    continue
                
                tmp = board[i][j]
                board[i][j] = 0
                
                if board[i][idx] == tmp:
                    board[i][idx] = 2*tmp
                    idx -= 1
                elif not board[i][idx]:
                    board[i][idx] = tmp
                else:
                    idx -= 1
                    board[i][idx] = tmp 
    
    elif direction == 2:  # up
        for j in range(n):
            idx = 0
            for i in range(1, n):
                if not board[i][j]:
                    continue
                    
                tmp = board[i][j]
                board[i][j] = 0
                
                if board[idx][j] == tmp:
                    board[idx][j] = 2*tmp
                    idx += 1
                elif not board[idx][j]:
                    board[idx][j] = tmp
                else:
                    idx += 1
                    board[idx][j] = tmp 
                
    else:  # down
        for j in range(n):
            idx = n-1
            for i in range(n-2, -1, -1):
                if not board[i][j]:
                    continue
                
                tmp = board[i][j]
                board[i][j] = 0
                
                if board[idx][j] == tmp:
                    board[idx][j] = 2*tmp
                    idx -= 1
                elif not board[idx][j]:
                    board[idx][j] = tmp
                else:
                    idx -= 1
                    board[idx][j] = tmp  
        
    for nxt_dir in range(4):
        backtracking(deepcopy(board), nxt_dir, times+1)
    
    
n = int(input())
initial_board = [list(map(int, input().split())) for _ in range(n)]

m = -1
for d in range(4):
    backtracking(deepcopy(initial_board), d, 0)
    
print(m)