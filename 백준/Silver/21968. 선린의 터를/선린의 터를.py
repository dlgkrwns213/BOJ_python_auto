import sys
input = sys.stdin.readline

ans = []
for _ in range(int(input())):
    n = bin(int(input()))[:1:-1]

    now, x = 0, 1
    for bit in n:
        if bit == '1':
            now += x
        x *= 3

    ans.append(now)
print('\n'.join(map(str, ans)))