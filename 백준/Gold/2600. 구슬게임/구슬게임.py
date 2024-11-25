# https://www.acmicpc.net/problem/2600
bs = list(map(int, input().split()))
for _ in range(5):
    k1, k2 = map(int, input().split())

    win = [[0]*(k2+1) for _ in range(k1+1)]
    for i in range(k1+1):
        for j in range(k2+1):
            x = 0
            for b in bs:
                if i >= b and not win[i-b][j]:
                    x = 1
            for b in bs:
                if j >= b and not win[i][j-b]:
                    x = 1

            win[i][j] = x

    print('A' if win[k1][k2] else 'B')