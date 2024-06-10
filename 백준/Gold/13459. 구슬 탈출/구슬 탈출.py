from collections import deque
INF = 10**9


def up(rx, ry, bx, by, ud, lr):
    nrx, nry, nbx, nby = rx, ry, bx, by
    rfin, bfin = False, False
    if ud < 0:
        # Red Ball
        for time in range(1, 10):
            rx -= 1
            if board[rx][ry] == 'O':
                nrx, nry = oi, oj
                rfin = True
                break
            if board[rx][ry] == '#':
                break
            
            nrx, nry = rx, ry
            
        # Blue Ball
        for time in range(1, 10):
            bx -= 1
            if board[bx][by] == 'O':
                nbx, nby = oi, oj
                bfin = True
                break
            if board[bx][by] == '#':
                break
            if (bx, by) == (nrx, nry):
                break
                
            nbx, nby = bx, by
            
    else:
        # Blue Ball
        for time in range(1, 10):
            bx -= 1
            if board[bx][by] == 'O':
                nbx, nby = oi, oj
                bfin = True
                break
            if board[bx][by] == '#':
                break
        
            nbx, nby = bx, by
            
        # Red Ball
        for time in range(1, 10):
            rx -= 1
            if board[rx][ry] == 'O':
                nrx, nry = oi, oj
                rfin = True
                break
            if board[rx][ry] == '#':
                break
            if (rx, ry) == (nbx, nby):
                break
            
            nrx, nry = rx, ry
    
    _ = None
    if bfin:
        return _, _, _, _, -1
    elif rfin:
        return _, _, _, _, 1
    else:
        return nrx, nry, nbx, nby, 0
    

def down(rx, ry, bx, by, ud, lr):
    nrx, nry, nbx, nby = rx, ry, bx, by
    rfin, bfin = False, False
    if ud > 0:
        # Red Ball
        for time in range(1, 10):
            rx += 1
            if board[rx][ry] == 'O':
                nrx, nry = oi, oj
                rfin = True
                break
            if board[rx][ry] == '#':
                break
            
            nrx, nry = rx, ry
            
        # Blue Ball
        for time in range(1, 10):
            bx += 1
            if board[bx][by] == 'O':
                nbx, nby = oi, oj
                bfin = True
                break
            if board[bx][by] == '#':
                break
            if (bx, by) == (nrx, nry):
                break
                
            nbx, nby = bx, by
            
    else:
        # Blue Ball
        for time in range(1, 10):
            bx += 1
            if board[bx][by] == 'O':
                nbx, nby = oi, oj
                bfin = True
                break
            if board[bx][by] == '#':
                break
        
            nbx, nby = bx, by
            
        # Red Ball
        for time in range(1, 10):
            rx += 1
            if board[rx][ry] == 'O':
                nrx, nry = oi, oj
                rfin = True
                break
            if board[rx][ry] == '#':
                break
            if (rx, ry) == (nbx, nby):
                break
            
            nrx, nry = rx, ry
    
    _ = None
    if bfin:
        return _, _, _, _, -1
    elif rfin:
        return _, _, _, _, 1
    else:
        return nrx, nry, nbx, nby, 0
    

def left(rx, ry, bx, by, ud, lr):
    nrx, nry, nbx, nby = rx, ry, bx, by
    rfin, bfin = False, False
    if lr < 0:
        # Red Ball
        for time in range(1, 10):
            ry -= 1
            if board[rx][ry] == 'O':
                nrx, nry = oi, oj
                rfin = True
                break
            if board[rx][ry] == '#':
                break
            
            nrx, nry = rx, ry
            
        # Blue Ball
        for time in range(1, 10):
            by -= 1
            if board[bx][by] == 'O':
                nbx, nby = oi, oj
                bfin = True
                break
            if board[bx][by] == '#':
                break
            if (bx, by) == (nrx, nry):
                break
                
            nbx, nby = bx, by
            
    else:
        # Blue Ball
        for time in range(1, 10):
            by -= 1
            if board[bx][by] == 'O':
                nbx, nby = oi, oj
                bfin = True
                break
            if board[bx][by] == '#':
                break
        
            nbx, nby = bx, by
            
        # Red Ball
        for time in range(1, 10):
            ry -= 1
            if board[rx][ry] == 'O':
                nrx, nry = oi, oj
                rfin = True
                break
            if board[rx][ry] == '#':
                break
            if (rx, ry) == (nbx, nby):
                break
            
            nrx, nry = rx, ry
    
    _ = None
    if bfin:
        return _, _, _, _, -1
    elif rfin:
        return _, _, _, _, 1
    else:
        return nrx, nry, nbx, nby, 0

def right(rx, ry, bx, by, ud, lr):
    nrx, nry, nbx, nby = rx, ry, bx, by
    rfin, bfin = False, False
    if lr > 0:
        # Red Ball
        for time in range(1, 10):
            ry += 1
            if board[rx][ry] == 'O':
                nrx, nry = oi, oj
                rfin = True
                break
            if board[rx][ry] == '#':
                break
            
            nrx, nry = rx, ry
            
        # Blue Ball
        for time in range(1, 10):
            by += 1
            if board[bx][by] == 'O':
                nbx, nby = oi, oj
                bfin = True
                break
            if board[bx][by] == '#':
                break
            if (bx, by) == (nrx, nry):
                break
                
            nbx, nby = bx, by
            
    else:
        # Blue Ball
        for time in range(1, 10):
            by += 1
            if board[bx][by] == 'O':
                nbx, nby = oi, oj
                bfin = True
                break
            if board[bx][by] == '#':
                break
        
            nbx, nby = bx, by
            
        # Red Ball
        for time in range(1, 10):
            ry += 1
            if board[rx][ry] == 'O':
                nrx, nry = oi, oj
                rfin = True
                break
            if board[rx][ry] == '#':
                break
            if (rx, ry) == (nbx, nby):
                break
            
            nrx, nry = rx, ry
    
    _ = None
    if bfin:
        return _, _, _, _, -1
    elif rfin:
        return _, _, _, _, 1
    else:
        return nrx, nry, nbx, nby, 0


def location(rx, ry, bx, by):
    x = rx-bx
    y = ry-by
    x = abs(x)//x if x else 0
    y = abs(y)//y if y else 0
    return x, y


def backtracking(rx, ry, bx, by, ud, lr, cnt):
    global ans
    if ans == cnt:
        return
    
    if cnt >= 10:
        return

    nrx, nry, nbx, nby, result = up(rx, ry, bx, by, ud, lr)
    if result == 1:
        ans = min(ans, cnt+1)
        fin = True
        return 
    elif result == 0:
        if (nrx, nry, nbx, nby) not in visited:
            visited.add((nrx, nry, nbx, nby))
            board[rx][ry] = '.'
            board[bx][by] = '.'
            board[nrx][nry] = 'R'
            board[nbx][nby] = 'B'
            nud, nlr = location(nrx, nry, nbx, nby)
            backtracking(nrx, nry, nbx, nby, nud, nlr, cnt+1)
            visited.remove((nrx, nry, nbx, nby))
            board[nrx][nry] = '.'
            board[nbx][nby] = '.'
            board[rx][ry] = 'R'
            board[bx][by] = 'B'
        
        
    nrx, nry, nbx, nby, result = down(rx, ry, bx, by, ud, lr)
    if result == 1:
        ans = min(ans, cnt+1)
        fin = True
        return 
    elif result == 0:
        if (nrx, nry, nbx, nby) not in visited:
            visited.add((nrx, nry, nbx, nby))
            board[rx][ry] = '.'
            board[bx][by] = '.'
            board[nrx][nry] = 'R'
            board[nbx][nby] = 'B'
            nud, nlr = location(nrx, nry, nbx, nby)
            backtracking(nrx, nry, nbx, nby, nud, nlr, cnt+1)
            visited.remove((nrx, nry, nbx, nby))
            board[nrx][nry] = '.'
            board[nbx][nby] = '.'
            board[rx][ry] = 'R'
            board[bx][by] = 'B'   
        
    nrx, nry, nbx, nby, result = left(rx, ry, bx, by, ud, lr)
    if result == 1:
        ans = min(ans, cnt+1)
        fin = True
        return 
    elif result == 0:
        if (nrx, nry, nbx, nby) not in visited:
            visited.add((nrx, nry, nbx, nby))
            board[rx][ry] = '.'
            board[bx][by] = '.'
            board[nrx][nry] = 'R'
            board[nbx][nby] = 'B'
            nud, nlr = location(nrx, nry, nbx, nby)
            backtracking(nrx, nry, nbx, nby, nud, nlr, cnt+1)
            visited.remove((nrx, nry, nbx, nby))
            board[nrx][nry] = '.'
            board[nbx][nby] = '.'
            board[rx][ry] = 'R'
            board[bx][by] = 'B'
                    
    nrx, nry, nbx, nby, result = right(rx, ry, bx, by, ud, lr)
    if result == 1:
        ans = min(ans, cnt+1)
        fin = True
        return 
    elif result == 0:
        if (nrx, nry, nbx, nby) not in visited:
            visited.add((nrx, nry, nbx, nby))
            board[rx][ry] = '.'
            board[bx][by] = '.'
            board[nrx][nry] = 'R'
            board[nbx][nby] = 'B'
            nud, nlr = location(nrx, nry, nbx, nby)
            backtracking(nrx, nry, nbx, nby, nud, nlr, cnt+1)
            visited.remove((nrx, nry, nbx, nby))
            board[nrx][nry] = '.'
            board[nbx][nby] = '.'
            board[rx][ry] = 'R'
            board[bx][by] = 'B'
    


n, m = map(int, input().split())
board = [[x for x in input()] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            ri, rj = i, j
        elif board[i][j] == 'B':
            bi, bj = i, j
        elif board[i][j] == 'O':
            oi, oj = i, j

UD, LR = location(ri, rj, bi, bj)
# rx, ry, bx, by, fin = right(ri, rj, bi, bj, UD, LR)
# print(fin)
# if fin == 0:
#     board[ri][rj] = "."
#     board[bi][bj] = "."
#     print(rx, ry, bx, by)
#     board[rx][ry] = "R"
#     board[bx][by] = "B"

#     for line in board:
#         print(*line)
        
visited = set()
visited.add((ri, rj, bi, bj))

ans = INF
backtracking(ri, rj, bi, bj, UD, LR, 0)
print(1 if ans != INF else 0)