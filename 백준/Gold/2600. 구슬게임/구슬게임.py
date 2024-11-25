# https://www.acmicpc.net/problem/2600
b1, b2, b3 = list(map(int, input().split()))
wins = [[False] * 531 for _ in range(531)]
for i in range(501):
    for j in range(501):
        enemy_lose = not any((wins[i-b1][j], wins[i-b2][j], wins[i-b3][j],
                              wins[i][j-b1], wins[i][j-b2], wins[i][j-b3]))
        wins[i][j] = enemy_lose

for _ in range(5):
    k1, k2 = map(int, input().split())
    print('B' if wins[k1][k2] else 'A')