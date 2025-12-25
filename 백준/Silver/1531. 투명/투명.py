n, m = map(int, input().split())

board = [[0]*101 for _ in range(101)]
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            board[i][j] += 1

print(sum(map(lambda line: sum(map(lambda x: int(x>m), line)), board)))