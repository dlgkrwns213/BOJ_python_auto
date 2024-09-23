def star(n, a, b, M):
    if n==3:
        for i in range(a, a+3):
            for j in range(b, b+3):
                M[i][j] = '*'
        M[a+1][b+1] = ' '
    else:
        for i in range(3):
            for j in range(3):
                if i==1 and j==1:
                    continue
                small_n = n//3
                new_a, new_b = i*small_n + a, j*small_n + b
                star(small_n, new_a, new_b, M)



n = int(input())
M = [[' ']*n for _ in range(n)]
star(n, 0, 0, M)

for m in M:
    print(''.join(m))
