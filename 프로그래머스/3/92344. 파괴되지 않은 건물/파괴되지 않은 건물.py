def solution(board, skill):
    answer = 0
    
    n, m = map(len, (board, board[0]))
    check = [[0]*(m+1) for _ in range(n+1)]
    for t, r1, c1, r2, c2, degree in skill:
        degree *= -1 if t == 1 else 1
        
        check[r1][c1] += degree 
        check[r2+1][c2+1] += degree
        check[r1][c2+1] -= degree 
        check[r2+1][c1] -= degree
        
    prefix = [[0]*(m+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(m):
            prefix[i][j] = prefix[i][j-1] + prefix[i-1][j] - prefix[i-1][j-1] + check[i][j]
        
    for i in range(n):
        for j in range(m):
            board[i][j] += prefix[i][j]
            
    answer = sum(map(lambda line: sum(x > 0 for x in line), board))

        
    return answer