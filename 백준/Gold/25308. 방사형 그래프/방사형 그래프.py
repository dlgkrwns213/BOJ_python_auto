# https://www.acmicpc.net/problem/25308
from itertools import permutations
get_mn = lambda x, y: (2 ** 0.5) * x * y / (x + y)

abilities = list(map(int, input().split()))

cnt = 0
for now in permutations(abilities, 8):
    possible = 1
    for i in range(8):
        x, y, z = now[i], now[i-1], now[i-2]
        if y < get_mn(x, z):
            possible = 0
            break

    cnt += possible
print(cnt)