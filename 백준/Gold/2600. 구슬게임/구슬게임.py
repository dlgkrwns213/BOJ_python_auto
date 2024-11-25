# https://www.acmicpc.net/problem/2600
b1, b2, b3 = list(map(int, input().split()))
for _ in range(5):
    k1, k2 = map(int, input().split())

    wins = [[0]*(k2+31) for _ in range(k1+31)]
    for i in range(k1+1):
        for j in range(k2+1):
            enemy_lose = not any((wins[i-b1][j], wins[i-b2][j], wins[i-b3][j],
                                  wins[i][j-b1], wins[i][j-b2], wins[i][j-b3]))
            wins[i][j] = enemy_lose

    print('B' if wins[k1][k2] else 'A')